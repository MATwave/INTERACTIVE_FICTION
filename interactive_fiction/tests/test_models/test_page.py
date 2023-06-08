import pytest


@pytest.mark.django_db
def test_book_page(book_page, book_item):
    # Проверяем, что у модели BookPage установлены ожидаемые значения
    assert book_page.title == 'Test Page'
    assert book_page.book.title == 'Test Book'
    assert book_page.body == 'Test page content'

    # Проверяем, что связь с BookItem работает
    assert book_page.items.count() == 0

    book_page.items.add(book_item)
    assert book_page.items.count() == 1
    assert book_page.items.first().name == 'Test Item'
