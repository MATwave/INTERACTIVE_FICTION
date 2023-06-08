import pytest


@pytest.mark.django_db
def test_page_link_has_all_required_items(page_link, book_item):
    # Создаем список предметов, необходимых для прохождения по ссылке
    required_items = [book_item]

    # Проверяем, что ссылка имеет все необходимые предметы
    assert page_link.has_all_required(required_items) is True


@pytest.mark.django_db
def test_page_link_missing_required_items(page_link):
    # Создаем список предметов, необходимых для прохождения по ссылке,
    # но не добавляем их к связи страницы
    required_items = []

    # Проверяем, что ссылка не имеет всех необходимых предметов
    assert page_link.has_all_required(required_items) is False
