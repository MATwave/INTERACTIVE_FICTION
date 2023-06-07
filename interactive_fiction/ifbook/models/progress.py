from django.contrib.auth.models import User
from django.db import models

from .book import Book
from .item import BookItem
from .page import BookPage


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
