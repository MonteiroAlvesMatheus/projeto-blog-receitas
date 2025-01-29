from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
from unittest.mock import patch

# Create your tests here.


class RecipeHomeViewsTest(RecipeTestBase):

    def test_recipe_home_view_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)

    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200)

    def test_recipe_home_view_loads_correct_templates(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_recipe_home_templates_shows_no_recipes_found_if_no_recipes(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(
            'No recipes published',
            response.content.decode('utf-8')
        )

    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()

        response = self.client.get(reverse('recipes:home'))
        content = response.content.decode('utf-8')
        response_context_recipe = response.context['recipes']

        self.assertIn('teste title', content)
        self.assertEqual(len(response_context_recipe), 1)

    def test_recipe_home_template_doesnt_load_recipes_not_published(self):
        self.make_recipe(is_published=False)

        response = self.client.get(reverse('recipes:home'))

        self.assertIn(
            'No recipes published',
            response.content.decode('utf-8')
        )

    def test_make_pagination_range_amount_of_recipes_per_page_is_and_current_page_correct(self):  # noqa E501
        self.make_recipe_in_batch(qtd=8)

        with patch('recipes.views.PER_PAGES', new=3):
            response = self.client.get(reverse('recipes:home'))
            response_context_recipe = response.context['recipes']
            paginator = response_context_recipe.paginator

            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)

            response_page = self.client.get(reverse('recipes:home')+'?page=1')
            self.assertEqual(response_page.status_code, 200)

            response_invalid = self.client.get(reverse('recipes:home')+'?page=one')
            response_context_recipe_invalid = response_invalid.context['recipes']
            self.assertEqual(response_context_recipe_invalid.number, 1)
