import pytest
from ifbook.models.item import BookItem


@pytest.mark.django_db
def test_bookitem_creation_and_str(book_item):
    # Проверка создания объекта
    assert book_item.name == "Test Item"
    assert BookItem.objects.count() == 1

    # Проверка метода __str__
    assert str(book_item) == "Test Item"
