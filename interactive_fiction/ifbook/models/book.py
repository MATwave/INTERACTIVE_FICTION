from django.db import models

from .page import BookPage

FIRST_PAGE_TITLE = "Первая страница"
FIRST_PAGE_BODY = "Это автоматически созданная первая страница твоей книги. " \
                  "Ты можешь поменять название и содержание в панели администратора"


class Book(models.Model):
    title = models.TextField(name="title", unique=True)
    first_page = models.ForeignKey("BookPage",
                                   null=True,
                                   blank=True,
                                   on_delete=models.SET_NULL,
                                   related_name="first_page")
    cover_art = models.ImageField(upload_to='books_cover', null=True)

    def __str__(self):
        return f"{self.title} ({self.id})"

    def save(self, *args, **kwargs):
        if not self.first_page:
            first_page = BookPage.objects.create(title=FIRST_PAGE_TITLE, body=FIRST_PAGE_BODY)
            self.first_page = first_page

            super().save(*args, **kwargs)  # Сохраняем Book, чтобы получить ID

            # Устанавливаем связь между книгой и первой страницей
            first_page.book = self
            first_page.save()
        else:
            super().save(*args, **kwargs)
