from django.views import View
from django.http.response import Http404
from recipes.models import Recipe
from authors.forms.recipe_form import RecipeForm
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipe(View):
    def get_recipe(self, id=None):
        recipe = None

        if id is not None:
            recipe = Recipe.objects.filter(
                is_published=False,
                author=self.request.user,
                pk=id,
            ).first()

            if not recipe:
                raise Http404()

        return recipe

    def render_recipe(self, form):
        return render(
            self.request,
            'authors/pages/dashboard_recipe.html',
            context={
                'form': form
            }
        )

    def get(self, request, id=None):

        recipe = self.get_recipe(id)

        form = RecipeForm(
            instance=recipe
        )

        return self.render_recipe(form)

    def post(self, request, id=None):
        recipe = self.get_recipe(id)

        form = RecipeForm(
            data=request.POST or None,
            files=request.FILES or None,
            instance=recipe
        )

        if form.is_valid():
            recipe = form.save(commit=False)

            recipe.author = request.user
            recipe.preparations_steps_is_html = False
            recipe.is_published = False

            recipe.save()

            messages.success(request, 'Your recipe has been saved successfully ')
            return redirect(reverse('authors:dashboard_recipe_edit', args=(recipe.id,)))

        return self.render_recipe(form)


@method_decorator(
    login_required(login_url='authors:login', redirect_field_name='next'),
    name='dispatch'
)
class DashboardRecipeDelete(DashboardRecipe):
    def post(self, *args, **kwargs):

        recipe = self.get_recipe(self.request.POST.get('id'))

        recipe.delete()

        messages.success(self.request, 'Deleted succesfully')
        return redirect(reverse('authors:dashboard'))
