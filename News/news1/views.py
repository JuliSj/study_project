from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
# from .forms import *


# def all_news(request):
#     return render(request, 'news1/all_news.html')

def all_news(request):
    #пример применения пользовательского менджера
    articles = Article.objects.all()
    a = articles.first()
    categories = Article.categories
    context={'today_articles': articles}
    author_list = User.objects.all()
    selected = 0
    if request.method=="POST":
        print(request.POST)
        selected = int(request.POST.get('author_filter'))
        if selected == 0:
            articles = Article.objects.all()
        else:
            articles = Article.objects.filter(author=selected)
        print(connection.queries)
    else:
        articles = Article.objects.all()
    context = {'articles': articles, 'author_list':author_list,'selected':selected,'categories':categories, }
    return render(request,'news1/all_news.html',context)
