from rest_framework import serializers
from core.bookstore.models import Product
from .category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(required=True, many=True)

    class Meta:
        model = Product
        fields = [
            'title',
            'active',
            'price',
            'category',
            'description',
        ]
