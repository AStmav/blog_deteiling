from django.urls import path,include
from . import views
from .views import  DoneView, FeedBackView, Get_callback





urlpatterns = [
    path('', views.index, name ='index'),
    path('callback/', Get_callback.as_view(), name='callback'),
    path('posts/', views.get_posts, name ='posts'),
    path('faq/', views.get_faq, name ='faq'),
    path('feedback/', views.FeedBackView, name ='feedback'),
    path('done/', DoneView.as_view(), name='done'),
    path('customer_feedback/', views.get_customer_feedback, name ='customer_feedback'),
    path('services/', views.get_services_info, name ='services'),
    path('contacts/', views.get_contacts, name ='contacts'),
    path('posts/<int:id_post>', views.get_one_post, name='one_of_post'),
    path('<int:sign_site>/', views.get_info_about_sign_by_number),
    path('<str:sign_site>/', views.get_info_about_sign, name='deteiling-name'),#динамический URL
]


