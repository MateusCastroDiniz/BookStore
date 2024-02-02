from rest_framework import serializers
from core.bookstore.models import Category


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]
