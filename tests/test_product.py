import pytest
from core.bookstore.factories import ProductFactory, CategoryFactory


@pytest.fixture
def product_created():
    category_test = CategoryFactory(title='teste')
    category_food = CategoryFactory(title='food')
    return ProductFactory(title='coxinha', category=[category_test, category_food])


@pytest.mark.django_db
def test_product_name(product_created):
    assert product_created.title == 'coxinha'


@pytest.mark.django_db
def test_product_category_title(product_created):
    for category in product_created.category.all():
        if 'food' in category.title:
            assert category.title == 'teste'
        return None
