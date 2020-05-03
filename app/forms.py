"""
Definition of forms.
"""


from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from django.db import models
from.models import Comment
from.models import Blog
from.models import videopost





class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'имя пользователя'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'пароль'}))


class CommentForm (forms.ModelForm):
    class Meta:
        model = Comment # используемая модель
        fields = ['text'] # требуется заполнить только поле text
        labels = {'text': "Комментарий"} # метка к полю формы text



class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog # используемая модель
        fields = ['title', 'description', 'content', 'posted', 'author', 'image'] # требуется заполнить только поле text
        labels = {'title': "Заголовок", 'description': "Краткое описание", 'content': "Содержание", 'posted': "Дата", 'author': "Автор", 'image': "Картинка", } # метка к полю формы text



class zayafkaForm(forms.Form):
    name = forms.CharField(label = 'Ваше имя:*', min_length=2, max_length=100)
    email = forms.EmailField(label = 'E-mail адрес:*', min_length=10)
    phone = forms.CharField(label = 'Ваш телефон:*', max_length=12)
    message = forms.CharField(label = 'Текст Сообщения:*', widget=forms.Textarea(attrs={'rows':12, 'cols':20}))



class videoForm(forms.ModelForm):
    class Meta:
        model = videopost 
        fields = ['title',  'author'] # требуется заполнить только поле text
        labels = {'title': "Заголовок", 'author': "Автор", } # метка к полю формы text
