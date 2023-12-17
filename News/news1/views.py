from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse_lazy
from .models import *
from django.db import connection, reset_queries
from django.views.generic import DetailView, DeleteView, UpdateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.paginator import Paginator
from .forms import *

def pagination(request):
    articles = Article.objects.all()
    p = Paginator(articles, 2)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'articles':page_obj}
    return render(request, 'news1/all_news.html', context)

import json
#URL:    path('search_auto/', views.search_auto, name='search_auto'),
def search_auto(request):
    print('Случился запрос!')
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        q = request.GET.get('term','')
        articles = Article.objects.filter(title__icontains=q)
        results =[]
        for a in articles:
            results.append(a.title)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data,mimetype)

from .utils import ViewCountMixin

class ArticleDetailView(ViewCountMixin, DetailView):
    model = Article
    template_name = 'news1/news_detail.html'
    context_object_name = 'article'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_object = self.object
        images = Image.objects.filter(article=current_object)
        context['images'] = images
        return context

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'news1/create_article.html'
    fields = ['title', 'anouncement', 'text', 'tags']

class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('news_index')
    template_name = 'news1/delete_article.html'

from users.utils import check_group # импортировали декоратор
@login_required(login_url=settings.LOGIN_URL)
@check_group('Authors') # пример использования декоратора
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            if current_user.id != None: #проверили что не аноним
                new_article = form.save(commit=False)
                new_article.author = current_user
                new_article.save() #сохраняем в БД
                form.save_m2m()
                for img in request.FILES.getlist('image_field'):
                    Image.objects.create(article=new_article, image=img, title=img.name)
                return redirect('news_index')
    else:
        form = ArticleForm()
    return render(request, 'news1/create_article.html', {'form':form})

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
