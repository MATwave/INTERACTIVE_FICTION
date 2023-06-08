import pytest
from ifbook.models.page_link import BookPage
from ifbook.models.progress import BookProgress


@pytest.mark.django_db
def test_start_reading(user, book):
    # Проверка метода start_reading
    progress = BookProgress.start_reading(user, book)
    assert progress.user == user
    assert progress.book == book
    assert progress.book_page == book.first_page


@pytest.mark.django_db
def test_reading_progress(user, book):
    # Проверка метода reading_progress при отсутствии прогресса чтения
    progress = BookProgress.reading_progress(user, book)
    assert progress is None

    # Создание прогресса чтения
    progress = BookProgress.objects.create(user=user, book=book, book_page=book.first_page)

    # Проверка метода reading_progress при наличии прогресса чтения
    retrieved_progress = BookProgress.reading_progress(user, book)
    assert retrieved_progress == progress


@pytest.mark.django_db
def test_save_progress(user, book):
    # Создание прогресса чтения
    progress = BookProgress.objects.create(user=user, book=book, book_page=book.first_page)

    # Сохранение прогресса чтения
    page = BookPage.objects.create(title='Test Page', book=book, body='Page content')
    progress.save_progress(page)

    # Проверка сохранения прогресса чтения
    updated_progress = BookProgress.objects.get(id=progress.id)
    assert updated_progress.book_page == page
