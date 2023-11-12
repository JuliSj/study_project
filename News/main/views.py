from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import SomeNews

def index(request):
    value = -10
    n1 = SomeNews('Новость1', 'Текст1', '07.11.23')
    n2 = SomeNews('Новость2', 'Текст2', '01.11.23')
    l = [n1, n2]
    context = {'title':'Страница главная',
               'Header1':'Заголовок страницы',
               'numbers': l,
               }
    return render(request, 'main/index.html', context)

def about(request):
    return HttpResponse('<h1> страница про нас </h1>')

def contacts(request):
    return HttpResponse('<h1> контакты </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')