import pytest
from core.bookstore.factories import *


@pytest.fixture
def order_created():
    user1 = UserFactory(username='Lucas')
    category = CategoryFactory(title='teste')
    product1 = ProductFactory(title='teste_product', category=[category])
    product2 = ProductFactory(title='teste2', category=[category])
    return OrderFactory(user=user1, product=[product1, product2])


@pytest.mark.django_db
def test_order_customer_name(order_created):
    assert order_created.user.username == 'Lucas'


@pytest.mark.django_db
def test_order_product_name(order_created):
    products = order_created.product.all()

    for product in products:
        if 'teste2' in product.title:
            assert product.title == 'teste2'
        return None
