from django.test import TestCase  # type: ignore
from recipes.models import Category, Recipe, User


class RecipeMixin:
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)

    def make_author(self,
                    username='teste_user',
                    email='teste@teste.com',
                    password='123',
                    first_name='testeuser',
                    last_name='teste'
                    ):
        return User.objects.create_user(
            username=username, email=email, password=password,
            first_name=first_name, last_name=last_name)

    def make_recipe(
            self,
            title='teste title',
            description='descrição teste',
            slug='recoe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation steps',
            preparations_steps_is_html=False,
            is_published=True,
            category_data=None,
            author_data=None):

        if category_data is None:
            category_data = {}

        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            title=title,
            description=description,
            slug=slug,
            preparation_time=preparation_time,
            preparation_time_unit=preparation_time_unit,
            servings=servings,
            servings_unit=servings_unit,
            preparation_steps=preparation_steps,
            preparations_steps_is_html=preparations_steps_is_html,
            is_published=is_published,
            category=self.make_category(**category_data),
            author=self.make_author(**author_data)
        )

    def make_recipe_in_batch(self, qtd=10):
        recipes = []
        for i in range(qtd):
            recipe = self.make_recipe(  # noqa F841
                title=f'receita{i} ', slug=f'slug-{i} ',
                author_data={'username': f'username{i} '})
            recipes.append(recipe)
        return recipes


class RecipeTestBase(TestCase, RecipeMixin):
    def setUp(self):
        return super().setUp()
