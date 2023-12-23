from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group

def profile(request):
    return render(request, 'users/profile.html')

from django.contrib.auth.decorators import login_required
from news1.models import Article
@login_required
def add_to_favorites(request, id):
    article = Article.objects.get(id=id)
    # проверяем, есть ли такая закладка с этой новостью
    bookmark = FavoriteArticle.objects.filter(user=request.user.id, article=article)
    if bookmark.exists():
        bookmark.delete()
        messages.warning(request, f"Новость {article.title} удалена из закладок")
    else:
        bookmark = FavoriteArticle.objects.create(user=request.user, article=article)
        messages.success(request, f"Новость {article.title} добавлена в закладки")
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

from .forms import AccountUpdateForm, UserUpdateForm
def profile_update(request):
    user = request.user
    account = Account.objects.get(user=user)
    if request.method == "POST":
        user_form = UserUpdateForm(request.POST, instance=user)
        account_form = AccountUpdateForm(request.POST, request.FILES, instance=account)
        if user_form.is_valid() and account_form.is_valid():
            user_form.save()
            account_form.save()
            messages.success(request,"Профиль успешно обновлен")
            return redirect('profile')
        else:
            pass
    else:
        context = {'account_form':AccountUpdateForm(instance=account),
                   'user_form':UserUpdateForm(instance=user)}
    return render(request,'users/edit_profile.html',context)

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            category = request.POST['account_type']
            if category == 'author':
                group = Group.objects.get(name='Actions Required')
                user.groups.add(group)
            else:
                group = Group.objects.get(name='Reader')
                user.groups.add(group)
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            account = Account.objects.create(user=user, nickname=user.username)
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, f'{username} был зарегистрирован!')
            return redirect('home')
    else:
        form = UserCreationForm()
    context = {'form':form}
    return render(request, 'users/registration.html', context)

def contact_page(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print('Сообщение отправлено', form.cleaned_data)
        else:
            print(form.errors)
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'users/contact_page.html', context)


def index(request):
    print(request.user, request.user.id)
    user_acc = Account.objects.get(user=request.user)
    print(user_acc, user_acc.birthdate, user_acc.gender)
    return HttpResponse('Приложение Users')

from django.core.paginator import Paginator
def my_news_list(request):
    articles = Article.objects.all()
    categories = Article.categories
    author = User.objects.get(id=request.user.id)
    selected = author.id
    articles = Article.objects.filter(author=selected)

    p = Paginator(articles,2)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    context = {'articles': page_obj, 'selected':selected,'categories':categories, }
    return render(request,'users/my_news_list.html',context)
