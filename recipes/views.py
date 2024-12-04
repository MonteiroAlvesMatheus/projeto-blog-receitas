from django.shortcuts import render
from __localcode.main import make_recipe
from .models import Recipe

# HTTP Request


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True).order_by('-id')

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
    })


def recipe(request, id):

    recipes = Recipe.objects.filter(id=id).order_by('-id')
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipes,
    })
