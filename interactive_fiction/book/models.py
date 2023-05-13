from __future__ import annotations

from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.TextField(name="title", unique=True)
