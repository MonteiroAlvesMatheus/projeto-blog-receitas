from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
# Create your tests here.


class RecipeViewsTest(RecipeTestBase):

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

    def test_recipe_category_view_is_correct(self):
        view = resolve(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertIs(view.func, views.category)

    def test_recipe_category_view_returns_status_code_404_if_not_found(self):
        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_category_template_loads_recipes(self):
        needed_title = 'This is a category test'

        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': 1})
        )
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_category_template_doesnt_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:category', kwargs={'category_id': recipe.category.id})
        )

        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_view_is_correct(self):
        view = resolve(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        self.assertIs(view.func, views.recipe)

    def test_recipe_detail_view_returns_status_code_404_if_not_found(self):
        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1000})
        )
        self.assertEqual(response.status_code, 404)

    def test_recipe_detail_template_loads_recipes(self):
        needed_title = 'This is a datail page - It Load one recipe'

        self.make_recipe(title=needed_title)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': 1})
        )
        content = response.content.decode('utf-8')

        self.assertIn(needed_title, content)

    def test_recipe_detail_template_doesnt_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)

        response = self.client.get(
            reverse('recipes:recipe', kwargs={'id': recipe.pk})
        )

        self.assertEqual(response.status_code, 404)
