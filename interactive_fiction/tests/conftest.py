import os
import shutil
import uuid

import pytest
from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import RequestFactory
from django.test.utils import override_settings
from ifbook.models.book import Book
from ifbook.models.item import BookItem
from ifbook.models.page import BookPage
from ifbook.models.page_link import PageLink


@pytest.fixture
def user():
    # Создание тестового пользователя
    return User.objects.create_user(username='testuser', password='testpassword')


@pytest.fixture
def cover_image(tmpdir):
    original_media_root = settings.MEDIA_ROOT  # Сохраняем исходное значение MEDIA_ROOT

    with override_settings(MEDIA_ROOT='test_media'):
        test_media_path = os.path.join(settings.MEDIA_ROOT)
        # Создаем временный файл изображения для обложки с уникальным именем
        filename = f'cover_{uuid.uuid4()}.jpg'
        file_path = tmpdir.join(filename)
        with open(file_path, 'wb') as f:
            f.write(b'')
        yield SimpleUploadedFile(name=filename, content=open(file_path, 'rb').read(), content_type='image/jpeg')
        os.remove(file_path)
        # Удаляем директорию test_media
        shutil.rmtree(test_media_path)

    settings.MEDIA_ROOT = original_media_root  # Восстанавливаем исходное значение MEDIA_ROOT


@pytest.fixture
def book(cover_image):
    # Создаем объект Book с обложкой
    return Book.objects.create(title='Test Book', cover_art=cover_image)


@pytest.fixture
def book_page(book):
    # Создаем объект BookPage и связываем его с book
    return BookPage.objects.create(title='Test Page', book=book, body='Test page content')


@pytest.fixture
def book_item():
    # Создание тестового предмета книги
    return BookItem.objects.create(name='Test Item')


@pytest.fixture
def page_link(book_page, book_item):
    # Создание связи страницы
    link = PageLink.objects.create(name='Test Link', from_page=book_page, to_page=book_page)
    link.items.add(book_item)
    return link


@pytest.fixture
def rf():
    return RequestFactory()
