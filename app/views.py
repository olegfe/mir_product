"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.db import models
from.models import Blog
from .models import Comment # использование модели комментариев
from .forms import CommentForm, BlogForm, zayafkaForm, videoForm  # использование формы ввода комментария

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )


def product(request):
    """Renders the product page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/product.html',
        {
            'title':'product Page',
            'year':datetime.now().year,
        }
    )

def registration(request):
 """Renders the registration page."""
 
 if request.method == "POST": # после отправки формы
    regform = UserCreationForm (request.POST)
    if regform.is_valid(): #валидация полей формы
        reg_f = regform.save(commit=False) # не сохраняем автоматиче
        reg_f.is_staff = False # запрещен вход в административный раздел
        reg_f.is_active = True # активный пользователь
        reg_f.is_superuser = False # не является суперпользователем
        reg_f.date_joined = datetime.now() # дата регистрации
        reg_f.last_login = datetime.now() # дата последней авторизации

        reg_f.save() # сохраняем изменения после добавления данных (добавление пользователя в БД пользователей)

        return redirect('home') # переадресация на главную страницу
 else:
     regform = UserCreationForm() # создание объекта формы для

 assert isinstance(request, HttpRequest)
 return render(
    request,
    'app/registration.html',
     {

        'regform': regform, # передача формы в шаблон веб-страницы

        'year':datetime.now().year,
    }
 )



def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.order_by('-posted') # запрос на выбор всех статей из модели, отсортированных по убыванию даты опубликования
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
            {       # параметр в {} — данные для использования в шаблоне.
            'title':'',
            'posts': posts, # передача списка статей в шаблон веб-страницы
            'year':datetime.now().year,
    }
)



def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr) # запрос на выбор конкретной статьи по параметру
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST": # после отправки данных формы на сер-вер методом POST
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user # добавляем (так как этого поля нет в форме) в модель Комментария (Comment) в поле автор авторизованного пользо-вателя
            comment_f.date = datetime.now() # добавляем в модель Комментария (Comment) текущую дату
            comment_f.post = Blog.objects.get(id=parametr) # добавляем в модель Ком-ментария (Comment) статью, для которой данный комментарий
            comment_f.save() # сохраняем изменения после добавления полей
            
            return redirect('blogpost', parametr=post_1.id) # переадресация на ту же страницу статьи после отправки комментария
    else:
        form = CommentForm() # создание формы для ввода комментария
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {
            'post_1': post_1, # передача конкретной статьи в шаблон веб-страницы
            'comments': comments, # передача всех комментариев к данной статье в шаблон веб-страницы
            'form': form, # передача формы в шаблон веб-страницы
            'year':datetime.now().year,
            
    }
)


def newpost(request):
    """Renders the videopost page."""
    if request.method == "POST":
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.posted = datetime.now()
        

            form.save()
            return redirect('blog')
    else:
        form = BlogForm ()


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/newpost.html',
        {
            'form':form,
            'year':datetime.now().year,
        }
    )

def zayafka(request):
    assert isinstance(request,HttpRequest)
    data = None 
    if request.method == "POST":
        form = zayafkaForm(request.POST)
        if form.is_valid():
            data = dict()
            data['name'] = form.cleaned_data['name']
            data['email'] = form.cleaned_data['email']
            data['phone'] = form.cleaned_data['phone']
            data['message'] = form.cleaned_data['message']
            form = None
    else :
        form = zayafkaForm()
    return render (
        request, 
        'app/zayafka.html',
        {
            'form': form,
            'data': data 
        }
     )




def videopost(request):
    """Renders the videopost page."""
    if request.method == "POST":
        form = videoForm(request.POST, request.FILES)
        if form.is_valid():

        

            form.save()
            return redirect('blog')
    else:
        form = videoForm ()


    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/videopost.html',
        {
            'title':'Видео',
            'message':'',
            'year':datetime.now().year,
        }
    )
