from django.db import models


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
