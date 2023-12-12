from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import Group

def profile(request):
    return render(request, 'users/profile.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            group = Group.objects.get(name='Authors')
            user.groups.add(group)
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