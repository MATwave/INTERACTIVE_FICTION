from __future__ import annotations

from django.db import models


class Book(models.Model):
    title = models.TextField(name="title", unique=True)  # Заголовок книги
    first_page = models.ForeignKey("BookPage",
                                   null=True,
                                   on_delete=models.SET_NULL,
                                   related_name="first_page")  # Ссылка на первую страницу книги
    cover_art = models.ImageField(upload_to='books_cover', null=True)

    def __str__(self):
        # Строковое представление модели Book
        return f"{self.title} ({self.id})"


class BookPage(models.Model):
    title = models.TextField(name="title")  # Заголовок страницы
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Ссылка на книгу, к которой относится страница
    body = models.TextField(name="body")  # Содержимое страницы

    def __str__(self):
        # Строковое представление модели BookPage
        return f"{self.title} ({self.id})"
