from django.urls import reverse, resolve
from recipes import views
from .test_recipe_base import RecipeTestBase
# Create your tests here.


class RecipeSearchViewsTest(RecipeTestBase):
    def test_recipe_search_view_is_correct(self):
        view = resolve(
            reverse('recipes:search')
        )
        self.assertIs(view.func, views.search)

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search')+'?search=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raises_404_if_no_search_term(self):
        url = reverse('recipes:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_scaped(self):
        url = reverse('recipes:search')+'?search=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

    def test_recipe_search_can_find_recipe_by_title(self):
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = self.make_recipe(title=title1, slug='one',
                                   author_data={'username': 'one'})
        recipe2 = self.make_recipe(title=title2, author_data={'username': 'two'})

        url_search = reverse('recipes:search')
        response1 = self.client.get(f'{url_search}?search={title1}')
        response2 = self.client.get(f'{url_search}?search={title2}')
        response3 = self.client.get(f'{url_search}?search=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])
        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response3.context['recipes'])
        self.assertIn(recipe2, response3.context['recipes'])

    def test_recipe_search_can_find_recipe_by_title(self):
        description1 = 'descriptions one'
        description2 = 'descriptions two'
        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = self.make_recipe(title=title1, description=description1, slug='one',
                                   author_data={'username': 'one'})
        recipe2 = self.make_recipe(
            title=title2, description=description2, author_data={'username': 'two'})

        url_search = reverse('recipes:search')
        response1 = self.client.get(f'{url_search}?search={description1}')
        response2 = self.client.get(f'{url_search}?search={description2}')
        response3 = self.client.get(f'{url_search}?search=descriptions')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])
        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response3.context['recipes'])
        self.assertIn(recipe2, response3.context['recipes'])
