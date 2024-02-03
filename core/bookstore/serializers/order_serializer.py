from rest_framework import serializers
from core.bookstore.models import Order, Product
from .product_serializer import ProductSerializer


class OrderSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True, many=True)
    products_id = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all(), write_only=True, many=True)
    total = serializers.SerializerMethodField()

    def get_total(self, instance):
        total = sum([product.price for product in instance.product.all()])
        return total

    def create(self, validated_data):
        product_data = validated_data.pop('products_id')
        user_data = validated_data.pop('user')

        # se der algum problema, talvez seja aqui!
        # mude user=user_data para **validated_data, ou faça o contrário.
        order = Order.objects.create(user=user_data)
        for product in product_data:
            order.product.add(product)

        return order

    class Meta:
        model = Order
        fields = [
            'product',
            'total',
            'user',
            'products_id'
        ]
