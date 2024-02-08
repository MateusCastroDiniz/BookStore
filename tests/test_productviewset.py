import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.bookstore.factories import *
from core.bookstore.models import *
from rest_framework.authtoken.models import Token


class TestProductViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()

        self.product = ProductFactory(title='produtoTeste', price=50.0)

    def test_get_products(self):

        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        response = self.client.get(reverse('product-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        product_data = json.loads(response.content)['results']

        self.assertEqual(product_data[0]['title'], self.product.title)

        self.assertEqual(product_data[0]['price'], self.product.price)
        self.assertEqual(product_data[0]['active'], self.product.active)

    def test_create_product(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)
        category = CategoryFactory()
        data = json.dumps({
            'title': 'celular',
            'price': 2000.0,
            'categories_id': [category.id,]
        })

        response = self.client.post(
            reverse('product-list'),
            data=data,
            content_type='application/json'
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_product = Product.objects.get(title='celular')

        self.assertEqual(created_product.title, 'celular')
        self.assertEqual(created_product.price, 2000.0)
