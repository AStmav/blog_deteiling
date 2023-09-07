from django.db import models
from django.core.validators import MinLengthValidator
from uuid import uuid4
import os
from phonenumber_field.modelfields import PhoneNumberField

class Question(models.Model):
    question = models.CharField(max_length=200,default='', null= False)
    answer = models.CharField(max_length=900,default='', null= False)

    def __str__(self):
        return f'{self.question}-{self.answer}'

class Services(models.Model):
    name_of_services = models.CharField(max_length=200,default='',null= False)
    price1 = models.CharField(max_length=200,default='',null= False)
    price2 = models.CharField(max_length=200,default='',null= False)

    def __str__(self):
        return f'{self.name_of_services}-{self.price1}-{self.price2}'

class Contacts(models.Model):
    tel_number = PhoneNumberField(unique = True, null = False, blank = False)
    address = models.CharField(max_length=40, default='',null=False)
    work_email = models.EmailField()

    def __str__(self):
        return f'{self.tel_number}-{self.address}-{self.work_email}'

class Author(models.Model):
    author = models.CharField(max_length=100)
    author_email= models.EmailField()
    def __str__(self):
        return f'{self.author}-{self.author_email}'

class Post(models.Model):
    publication_date = models.DateTimeField(blank=True)
    title = models.CharField(max_length=250)
    content = models.TextField()
    short_content =models.TextField(default='', null= False)

    def __str__(self):
        return f'{self.title}-{self.content}-{self.publication_date}'


class Callback(models.Model):
    yourname = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    telnumber = PhoneNumberField(unique = True, null = False, blank = False)
    message = models.TextField(max_length=1000)

class Photo(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='posts/', height_field=None,width_field=None, max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

def get_file_path(instance, filename):
    ext = filename.split('.')[-1] #генерируем случайное имя файла
    filename = f'{uuid4()}.{ext}'
    return os.path.join('my_data/', filename) #возвращаем путь к файлу

class Feedback(models.Model):
    name = models.CharField(max_length=10, validators=[MinLengthValidator(2)])
    telephone_num = PhoneNumberField(unique = True, null = False, blank = False)
    publication_date = models.DateTimeField(auto_now_add=True)
    mail = models.EmailField()
    avto = models.CharField(max_length=20)
    feedback = models.CharField(max_length=400)
    image = models.ImageField(null=True, blank=True,upload_to=get_file_path, height_field=None, width_field=None, max_length=100)

class IndexPage(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()
    image = models.ImageField(null=True, blank= True, upload_to = 'my_data_index_page/',height_field=None, width_field=None, max_length=100)










