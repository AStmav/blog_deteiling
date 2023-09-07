from django import forms
from .models import Feedback, Callback
from django.forms import Textarea


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields ='__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя'}),
            'telephone_num': forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'mail': forms.TextInput(attrs={'placeholder': 'Введите e-mail'}),
            'avto': forms.TextInput(attrs={'placeholder': 'Марка автомобиля'}),
            'feedback': forms.Textarea(attrs={'placeholder': 'Введите текст отзыва'}),
            'image': forms.FileInput(attrs={'placeholder': 'Добавить изображение'})
        }
        error_messages = {
            'name': {
                'min_lenght': 'Слишком мало символов',
                'required':'Обязательно к заполнению'
            }
        }

class CallbackForm(forms.ModelForm):

    class Meta:
        model = Callback
        fields = ['yourname', 'email', 'telnumber','message']
        widgets = {
            'yourname': forms.TextInput(attrs={'placeholder': 'Ваше имя '}),
            'email': forms.TextInput(attrs={'placeholder': 'Введите e-mail'}),
            'telnumber':forms.TextInput(attrs={'placeholder': 'Номер телефона'}),
            'message': Textarea(
                attrs={
                    'placeholder': 'Напишите тут ваше сообщение'
                }
            )
        }




