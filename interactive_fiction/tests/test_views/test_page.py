import pytest
from django.urls import reverse
from ifbook.models.progress import BookProgress
from ifbook.views import PageView


@pytest.mark.django_db
def test_page_view(rf, book, book_page, page_link, user):
    # Создание экземпляра PageView
    view = PageView()
    BookProgress.start_reading(user=user, book=book)

    # Создание тестового запроса
    url = reverse("page", kwargs={"book_id": book.id, "page_id": book.first_page_id})
    request = rf.get(url)
    request.user = user

    # Вызов метода get() PageView с тестовым запросом
    response = view.get(request, book_id=book.id, page_id=book_page.id)

    # Проверка возвращаемого значения при наличии прогресса
    assert response.status_code == 200

    # Проверка сохранения прогресса чтения
    progress = BookProgress.reading_progress(user=user, book=book.id)
    assert progress.book_page.id == book_page.id

    # Проверка перенаправления при отсутствии прогресса чтения
    no_progress_request = rf.get(url)
    no_progress_request.user = user
    progress.delete()  # Удаление прогресса чтения
    no_progress_response = view.get(no_progress_request, book_id=book.id, page_id=book_page.id)
    assert no_progress_response.status_code == 302
    assert no_progress_response.url == reverse("book", kwargs={"book_id": book.id})
