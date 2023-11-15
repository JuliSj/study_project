from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import SomeNews, Product

def index(request):
    # value = -10
    # n1 = SomeNews('Новость1', 'Текст1', '07.11.23')
    # n2 = SomeNews('Новость2', 'Текст2', '01.11.23')
    # l = [n1, n2]
    # context = {'title':'Страница главная',
    #            'Header1':'Заголовок страницы',
    #            'numbers': l,
    #            }
    if request.method == 'POST':
        print('Получили post-запрос!')
        print(request.POST)
        title = request.POST.get('title')
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        new_product = Product(title, float(price), int(quantity))
        print('Создан товар:', new_product.title, 'Общая сумма:', new_product.amount())
    else:
        print('Получили get-запрос!')
    water = Product('Добрый-минералка', 43, 2)
    chocolate = Product('Шоколадка', 80, 1)

    colors = ['red', 'blue', 'golden', 'black']
    context = {
        'colors': colors,
        'water': water,
        'chocolate': chocolate,
    }
    return render(request, 'main/index.html', context)


def get_demo(request,a,operation,b):
    result = 0
    if operation == 'plus':
        result = int(a)+ int(b)
    elif operation == 'minus':
        result = int(a) - int(b)
    elif operation == 'multiply':
        result = int(a) * int(b)
    elif operation == 'divide':
        result = int(a) / int(b)
    else:
        return HttpResponse(f'Неверная команда')
    return HttpResponse(f'Вы ввели: {a} и {b} <br>Результат {operation}: {result}')

def about(request):
    return HttpResponse('<h1> страница про нас </h1>')

def contacts(request):
    return HttpResponse('<h1> контакты </h1>')

def sidebar(request):
    return render(request, 'main/sidebar.html')

def custom_404(request, exception):
    #return render(request, 'main/sidebar.html')
    return HttpResponse(f'Ой-ёй-ёй! Какая жалость!:{exception}')