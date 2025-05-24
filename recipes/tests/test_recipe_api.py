from django.urls import reverse
from rest_framework import test

from recipes.tests.test_recipe_base import RecipeMixin


class RecipeAPIv2Test(test.APITestCase, RecipeMixin):
    def test_recipe_api_list_returns_status_code_200(self):
        response = self.client.get(reverse('recipes:recipes-api-list'))
        self.assertEqual(response.status_code, 200)
