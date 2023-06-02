from django.test import TestCase, RequestFactory
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Recipe
from .views import RecipeListView, RecipeDescriptionView


class RecipeListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
       
        self.recipe1 = Recipe.objects.create(
            recipe_name='Recipe 1',
            recipe_description='Recipe 1 description'
        )
        self.recipe2 = Recipe.objects.create(
            recipe_name='Recipe 2',
            recipe_description='Recipe 2 description'
        )

    def test_recipe_list_view(self):
        url = reverse('recipe-list')
        request = self.factory.get(url)
        request.user = self.user

        response = RecipeListView.as_view()(request)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'admin_templates/product_list.html')
        self.assertContains(response, self.recipe1.recipe_name)
        self.assertContains(response, self.recipe2.recipe_name)


