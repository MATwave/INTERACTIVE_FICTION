import pytest
from ifbook.models.book import Book
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client):
    # Создание тестовых данных
    book1 = Book.objects.create(title="Book 1")
    book2 = Book.objects.create(title="Book 2")

    # Выполнение GET-запроса к IndexView
    response = client.get("/")

    # Проверка, что возвращается ожидаемый шаблон
    assert response.status_code == 200
    assertTemplateUsed(response, "book_index.html")

    # Проверка, что контекст содержит ожидаемые книги
    assert list(response.context["books"]) == [book1, book2]
