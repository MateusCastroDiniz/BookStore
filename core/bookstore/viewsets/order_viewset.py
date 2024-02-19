from rest_framework.viewsets import ModelViewSet

from core.bookstore.models import Order
from core.bookstore.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import (
    SessionAuthentication,
    BasicAuthentication,
    TokenAuthentication,
)


class OrderViewSet(ModelViewSet):
    authentication_classes = [
        SessionAuthentication,
        BasicAuthentication,
        TokenAuthentication,
    ]
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all().order_by("-id")
