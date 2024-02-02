import pytest
from core.bookstore.factories import CategoryFactory


@pytest.fixture
def category_created():
    return CategoryFactory(title='comida')


@pytest.mark.django_db
def test_category(category_created):
    assert category_created.title == 'comida'
