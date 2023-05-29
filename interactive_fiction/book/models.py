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


class PageLink(models.Model):
    name = models.TextField()  # Название ссылки
    from_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)  # Ссылка на исходную страницу
    to_page = models.ForeignKey(BookPage,
                                related_name="to_page",
                                on_delete=models.CASCADE)  # Ссылка на целевую страницу

    def __str__(self):
        # Строковое представление модели PageLink
        return f"{self.from_page.title} -> {self.to_page.title} ({self.id})"

    class Meta:
        # Уникальность комбинации исходной и целевой страницы для модели PageLink
        unique_together = ["from_page", "to_page"]
