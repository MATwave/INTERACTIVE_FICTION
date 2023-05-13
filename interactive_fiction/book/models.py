from __future__ import annotations

from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(name="title", unique=True)
    first_page = models.ForeignKey("BookPage", null=True, on_delete=models.SET_NULL, related_name="first_page")

    def __str__(self):
        return f"{self.title} ({self.id})"


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField(name="title")
    body = models.TextField(name="body")

    def __str__(self):
        return f"{self.title} ({self.id})"


class PageLink(models.Model):
    from_page = models.ForeignKey(BookPage, on_delete=models.CASCADE)
    to_page = models.ForeignKey(BookPage, related_name="to_page", on_delete=models.CASCADE)

    name = models.TextField()

    def __str__(self):
        return f"{self.from_page.title} -> {self.to_page.title} ({self.id})"

    class Meta:
        unique_together = ["from_page", "to_page"]
