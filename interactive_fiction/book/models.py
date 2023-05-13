from __future__ import annotations

from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(name="title", unique=True)


class BookPage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    title = models.TextField(name="title")
    body = models.TextField(name="body")
