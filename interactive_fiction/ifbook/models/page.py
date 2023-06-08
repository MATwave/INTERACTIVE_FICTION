from django.db import models


class BookPage(models.Model):
    title = models.TextField(name="title")
    book = models.ForeignKey("Book", null=True, blank=True, on_delete=models.CASCADE)
    body = models.TextField(name="body")
    items = models.ManyToManyField("BookItem", blank=True)

    def __str__(self):
        return f"{self.title} ({self.id})"
