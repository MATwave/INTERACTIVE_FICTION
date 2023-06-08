import pytest
from ifbook.models.book import Book


@pytest.mark.django_db
@pytest.mark.django_temporary_media_root
def test_book_creation(cover_image):
    # Создаем объект Book
    book = Book.objects.create(title='Test Book', cover_art=cover_image)

    # Проверяем, что объект был создан
    assert book.id is not None

    # Проверяем значения полей объекта
    assert book.title == 'Test Book'
    assert book.first_page is not None
    assert 'books_cover/cover' in book.cover_art.name

    # Проверяем метод __str__
    assert str(book) == f'Test Book ({book.id})'

    # Проверяем, что при сохранении объекта без first_page, создается новая страница
    book_without_first_page = Book.objects.create(title='Book Without First Page', cover_art=cover_image)
    assert book_without_first_page.first_page is not None
    assert book_without_first_page.first_page.title == 'Первая страница'

    # Проверяем, что созданная страница привязана к книге
    assert book_without_first_page.first_page.book_id == book_without_first_page.id
