from django.db import models
from .product import Product
from django.contrib.auth.models import User


class Order(models.Model):
    product = models.ManyToManyField(Product, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido de {self.user.username}: {[product.title for product in self.product.all()]}"
