from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.core.mail import send_mail

from .models import Post, Question,Feedback, Services, Contacts, IndexPage, Photo, Callback
from .forms import FeedBackForm, CallbackForm

from django.views.generic import CreateView
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView



# Create your views here.
def home(request):
    return HttpResponse('Блог детейлера, или как все начиналось.')


site_map={
    #'faq': 'Часто задаваемый вопросы по нашим услугам.',
    'contacts': 'Нащ адрес: Улица калашникова. Контактный телефон: 8(924-866-21-75)',
    'services': 'Каталог наших услуг',
    # 'posts': 'Записки сумасшедшего',
    'feedback':'Обратная связь'
}




def index(request):#страница меню
    index_post = IndexPage.objects.all()
    return  render(request, 'blog_deteiling/index.html', context={'index_post':index_post})


#
def get_menu_item_title(request):
    menu_title= list(menu_item_title)
    context1 = {
       'menu_title':menu_title
    }
    return render(request, 'includes/navbar.html', context= context1)

def get_info_about_sign(request, sign_site: str): #динамический вывод содержимого страницы

    description = site_map.get(sign_site)
    data ={
        'description_blog_deteiling':description,
        'sign':sign_site
    }

    return render(request, 'blog_deteiling/info_deteiling.html', context=data)
    #return render(request, 'includes/navbar.html', context=data)


def get_info_about_sign_by_number(request, sign_site: int): #настраиваем redirect, обращение к категориям по номеру
    categories_site=list(site_map)
    if sign_site > len(categories_site):
        return HttpResponseNotFound('Страница не найденна. Обратитесь в техническу поддержку. :)')

    else:
        name_page=categories_site[sign_site-1]
    redirect_url = reverse('deteiling-name', args =(name_page, )) #redirect url blog_deteiling/'pages'
    return HttpResponseRedirect(redirect_url)

def get_posts(request):
    posts = Post.objects.all()
    return render(request,'blog_deteiling/posts.html',
                  {'posts': posts})

def get_one_post(request, id_post:int): #выводим отдельный пост
    onepost = Post.objects.get(id=id_post)# из колонки id выбираем нужный нам id поста
    photos = Photo.objects.filter(post=onepost)
    return render(request,'blog_deteiling/one_post.html',
                  {'onepost': onepost, 'photos': photos})


def get_faq(request):
    faq_list =Question.objects.all()
    return render(request, 'blog_deteiling/faq.html', {'faq_list': faq_list})


def FeedBackView(request):
    if request.method == 'POST':
        form = FeedBackForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            img_obj = form.instance
            return render(request, 'blog_deteiling/feedback.html', {'form': form, 'img_obj': img_obj})
    else:
        form = FeedBackForm()
    return render(request, 'blog_deteiling/feedback.html', context={'form': form})

class DoneView(TemplateView):
    template_name = 'blog_deteiling/done.html'





def get_customer_feedback(request):
    reviews = Feedback.objects.all()
    return render(request, 'blog_deteiling/customer_feedback.html', context={'reviews':reviews})


def get_services_info(request):
    services_info = Services.objects.all()
    return render(request, 'blog_deteiling/services.html', context={'services_info':services_info})

def get_contacts(request):
    contacts_info = Contacts.objects.all()
    return render(request, 'blog_deteiling/contacts.html', context={'contacts_info':contacts_info})

class Get_callback(CreateView):
    model = Callback
    # fields = ["first_name", "last_name", "message"]
    success_url = reverse_lazy('success_page')
    form_class = CallbackForm

    def form_valid(self, form):
        data = form.data
        subject = f'Сообщение с формы от {data["yourname"]} {data["telnumber"]} Почта отправителя: {data["email"]}'
        email(subject, data['message'])
        return super().form_valid(form)

def email(subject, content):
    send_mail(subject,
              content,
              'отправитель@gmail.com',
              ['получатель1@gmail.com']
              )


def success(request):
    return HttpResponse('Письмо отправлено!')

