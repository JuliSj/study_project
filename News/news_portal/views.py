from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'news_portal/index.html')

def single(request):
    return render(request, 'news_portal/single.html')

def all_news(request):
    return render(request, 'news_portal/all_news.html')

def account(request):
    return render(request, 'news_portal/account.html')