from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Hello', '123'],
        'obj': {
            'name': 'Ann',
            'age': '17',
            'hobby': 'Painting'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, template_name='main/contact.html')


def help(request):
    return render(request, template_name='main/help.html')