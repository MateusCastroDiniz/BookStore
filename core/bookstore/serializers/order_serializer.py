from rest_framework import serializers
from core.bookstore.models import Order
from .category_serializer import CategorySerializer
from .product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(required=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    class Meta:
        model = Order
        fields = [
            'product',
            'total',
        ]
