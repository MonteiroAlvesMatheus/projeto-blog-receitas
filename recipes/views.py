from django.shortcuts import render


# HTTP Request


def home(request):
    return render(request, 'recipes/home.html')
