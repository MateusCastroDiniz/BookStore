from rest_framework import serializers
from core.bookstore.models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'description',
            'active',
        ]

