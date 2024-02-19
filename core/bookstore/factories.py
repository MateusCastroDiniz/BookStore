import factory

from django.contrib.auth.models import User
from .models.product import Product
from .models.order import Order
from .models.category import Category


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker("pystr")
    email = factory.LazyAttribute(lambda x: "%s@exemple.com" % x.username)

    class Meta:
        model = User


class CategoryFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    slug = factory.Faker("pystr")
    description = factory.Faker("pystr")
    active = factory.Iterator([True, False])

    class Meta:
        model = Category


class ProductFactory(factory.django.DjangoModelFactory):
    title = factory.Faker("pystr")
    price = factory.Faker("pyfloat")
    category = factory.LazyAttribute(CategoryFactory)

    @factory.post_generation
    def category(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for category in extracted:
                self.category.add(category)

    class Meta:
        model = Product
        skip_postgeneration_save = True


class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for product in extracted:
                self.product.add(product)

    class Meta:
        model = Order
        skip_postgeneration_save = True
