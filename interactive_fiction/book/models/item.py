from __future__ import annotations

from django.db import models


class Item(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"
