from django.contrib import admin
from .models import Post, Question, Author,Feedback, Services, Contacts, IndexPage, Photo, Callback
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
    pass

class PhotoInline(admin.StackedInline):
    model = Photo
    max_num = 10
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]
    list_display = ['title', 'short_content',]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question','answer']
    list_editable = ['answer']
    list_per_page = 15

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author','author_email']

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name','telephone_num','mail','avto','feedback','publication_date', 'image']

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name_of_services', 'price1','price2']

class ContactsAdmin(admin.ModelAdmin):
    list_display = ['tel_number','address','work_email']

class IndexPageAdmin(admin.ModelAdmin):
    list_display = ['title','content','image']

class CallbackAdmin(admin.ModelAdmin):
    list_display = ['yourname','telnumber','message']

admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(IndexPage, IndexPageAdmin)
admin.site.register(Callback,CallbackAdmin)

