from recipes.tests.test_recipe_base import RecipeTestBase
from django.urls import reverse


class PaginationRecipeTest(RecipeTestBase):
    def test_home_page_displays_9_recipes_when_9_created(self):
        for c in range(9):
            self.make_recipe(
                slug=f'recipe{c}',
                author_data={'username': f'test{c}'}
            )

        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(len(response.context['recipes']), 9)

    def test_home_page_displays_max_9_recipes_when_more_than_9_created(self):
        for c in range(10):
            self.make_recipe(
                slug=f'recipe{c}',
                author_data={'username': f'test{c}'}
            )

        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(len(response.context['recipes']), 9)
