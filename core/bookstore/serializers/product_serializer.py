from rest_framework import serializers
from core.bookstore.models import Product, Category
from .category_serializer import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    categories_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), write_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            'id',
            'title',
            'active',
            'price',
            'category',
            'categories_id',
            'description',
        ]

    def create(self, validated_data):
        category_data = validated_data.pop('categories_id')

        # se der algum problema, olhe aqui!!!
        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
            return product
