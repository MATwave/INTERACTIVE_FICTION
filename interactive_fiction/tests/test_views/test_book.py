import pytest
from pytest_django.asserts import assertTemplateUsed


@pytest.mark.django_db
def test_index_view(client, book):
    # Выполнение GET-запроса к IndexView
    response = client.get("/")

    # Проверка, что возвращается ожидаемый шаблон
    assert response.status_code == 200
    assertTemplateUsed(response, "book_index.html")

    # Проверка, что контекст содержит ожидаемые книги
    assert list(response.context["books"]) == [book]
