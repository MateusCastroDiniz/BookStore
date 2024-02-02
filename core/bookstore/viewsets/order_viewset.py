from rest_framework.viewsets import ModelViewSet

from core.bookstore.models import Order
from core.bookstore.serializers import OrderSerializer


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.all()
