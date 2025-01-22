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
