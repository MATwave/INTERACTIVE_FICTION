import pytest
from django.urls import reverse
from ifbook.models.progress import BookProgress
from ifbook.views import TakeView


@pytest.mark.django_db
def test_take_view(rf, book, book_page, book_item, user):
    # Создание экземпляра TakeView
    view = TakeView()
    BookProgress.start_reading(user=user, book=book)

    # Создание тестового запроса
    url = reverse("take", kwargs={"book_id": book.id, "page_id": book_page.id, "item_id": book_item.id})
    request = rf.get(url)
    request.user = user

    # Вызов метода get() TakeView с тестовым запросом
    response = view.get(request, book_id=book.id, page_id=book_page.id, item_id=book_item.id)

    # Проверка перенаправления на страницу после взятия предмета
    assert response.status_code == 302
    assert response.url == reverse('page', kwargs={'book_id': book.id, 'page_id': book_page.id})

    # Проверка добавления предмета в прогресс чтения
    progress = BookProgress.reading_progress(user=user, book=book.id)
    assert book_item in progress.items.all()

    # Проверка перенаправления при отсутствии прогресса чтения
    no_progress_request = rf.get(url)
    no_progress_request.user = user
    progress.delete()  # Удаление прогресса чтения
    no_progress_response = view.get(no_progress_request, book_id=book.id, page_id=book_page.id, item_id=book_item.id)
    assert no_progress_response.status_code == 302
    assert no_progress_response.url == reverse("book", kwargs={"book_id": book.id})
