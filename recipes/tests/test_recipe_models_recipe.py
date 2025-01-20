from .test_recipe_base import RecipeTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(RecipeTestBase):
    def setUp(self):
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defalts(self):
        recipe = Recipe(
            title='teste title',
            description='descrição teste',
            slug='recoe-slug',
            preparation_time=10,
            preparation_time_unit='Minutos',
            servings=5,
            servings_unit='Porções',
            preparation_steps='Recipe Preparation steps',
            category=self.make_category(name='test Default Category'),
            author=self.make_author(username='newuser')
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    @parameterized.expand(
        [
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65),
        ]
    )
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defalts()
        self.assertFalse(
            recipe.preparations_steps_is_html,
            msg='Recipe preparation_steps_is_html is not False'
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defalts()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published is not False'
        )

    def test_recipe_string_representation(self):
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(
            str(self.recipe), 'Testing Representation',
            msg='Recipe string representation must be recipe title'
        )
