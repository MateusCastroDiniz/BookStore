from rest_framework.viewsets import ModelViewSet
from core.bookstore.models import Product
from core.bookstore.serializers import ProductSerializer

class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
