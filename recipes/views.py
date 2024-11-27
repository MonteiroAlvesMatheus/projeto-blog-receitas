from django.shortcuts import render
from django.http import HttpResponse

# HTTP Request


def home(request):
    return render(request, 'recipes/home.html')


def contato(request):
    return render(request, 'recipes/contato.html')


def sobre(request):
    return HttpResponse('sobre')
