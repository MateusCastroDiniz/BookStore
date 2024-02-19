from django.urls import path, include
from rest_framework import routers
from core.bookstore.viewsets import OrderViewSet, ProductViewSet, CategoryViewSet

OrderRouter = routers.SimpleRouter()
OrderRouter.register(r"order", OrderViewSet, basename="order")

ProductRouter = routers.SimpleRouter()
ProductRouter.register(r"product", ProductViewSet, basename="product")

CategoryRouter = routers.SimpleRouter()
CategoryRouter.register(r"category", CategoryViewSet, basename="category")

urlpatterns = [
    path("", include(OrderRouter.urls)),
    path("", include(ProductRouter.urls)),
    path("", include(CategoryRouter.urls)),
]
