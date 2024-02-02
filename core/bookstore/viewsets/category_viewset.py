from rest_framework.viewsets import ModelViewSet
from core.bookstore.models import Category
from core.bookstore.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
