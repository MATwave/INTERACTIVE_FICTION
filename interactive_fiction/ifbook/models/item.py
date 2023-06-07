from django.db import models


class BookItem(models.Model):
    name = models.TextField()

    def __str__(self):
        return f"{self.name}"
