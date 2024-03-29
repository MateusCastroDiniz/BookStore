import json
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from core.bookstore.factories import (
    ProductFactory,
    OrderFactory,
    CategoryFactory,
    UserFactory,
)
from core.bookstore.models import Product, Category, Order
from rest_framework.authtoken.models import Token


class TestOrderViewSet(APITestCase):
    client = APIClient()

    def setUp(self):
        self.user = UserFactory()
        token = Token.objects.create(user=self.user)
        token.save()
        self.category = CategoryFactory(title="stationary's")
        self.product = ProductFactory(
            title="Papel", price=1000.0, category=[self.category]
        )
        self.order = OrderFactory(product=[self.product])

    def test_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        response = self.client.get(reverse("order-list"))

        # import pdb; pdb.set_trace()

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        order_data = json.loads(response.content)["results"][0]["product"]
        self.assertEqual(order_data[0]["title"], self.product.title)
        self.assertEqual(order_data[0]["price"], self.product.price)
        self.assertEqual(order_data[0]["description"], self.product.description)
        self.assertEqual(order_data[0]["category"][0]["title"], self.category.title)

    def test_create_order(self):
        token = Token.objects.get(user__username=self.user.username)
        self.client.credentials(HTTP_AUTHORIZATION="Token " + token.key)
        user = UserFactory()
        product = ProductFactory()
        data = json.dumps({"products_id": [product.id], "user": user.id})

        response = self.client.post(
            reverse("order-list"), data=data, content_type="application/json"
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_order = Order.objects.get(user=user)
