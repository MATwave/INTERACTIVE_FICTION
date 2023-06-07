from __future__ import annotations

from django.contrib.auth.models import User
from django.db import models

from .item import BookItem


class Book(models.Model):
    title = models.TextField(name="title", unique=True)
    first_page = models.ForeignKey("BookPage",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="first_page")  # Ссылка на первую страницу книги
    cover_art = models.ImageField(upload_to='books_cover', null=True)

    def __str__(self):
        return f"{self.title} ({self.id})"


class BookPage(models.Model):
    title = models.TextField(name="title")
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(name="body")
    items = models.ManyToManyField(BookItem, blank=True)

    def __str__(self):
        return f"{self.title} ({self.id})"


class BookProgress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Ссылка на книгу, к которой относится страница
    book_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    items = models.ManyToManyField(BookItem, blank=True)

    class Meta:
        unique_together = ['user', 'book']

    @classmethod
    def start_reading(cls, user, book):
        progress = BookProgress(user=user, book=book, book_page=book.first_page)
        progress.save()
        return progress

    @classmethod
    def reading_progress(self, user, book):
        try:
            progress = BookProgress.objects.get(book=book, user=user)
        except BookProgress.DoesNotExist:
            return None

        return progress

    def save_progress(self, page_id):
        self.book_page = page_id
        self.save()
