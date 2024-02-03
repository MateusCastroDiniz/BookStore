import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.bookstore.factories import *
from core.bookstore.models import *


class TestCategoryViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.category = CategoryFactory(title='categoriaTeste')

    def test_get_category(self):
        response = self.client.get(reverse('category-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        category_data = json.loads(response.content)
        self.assertEqual(category_data[0]['title'], self.category.title)

    def test_create_category(self):
        data = json.dumps({
            'title': 'testando123'
        })
        response = self.client.post(reverse('category-list'), data=data, content_type='application/json')

        # import pdb
        #
        # pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_category = Category.objects.get(title='testando123')
        self.assertEqual(created_category.title, 'testando123')
