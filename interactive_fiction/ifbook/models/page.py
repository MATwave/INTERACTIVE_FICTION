from __future__ import annotations

from django.db import models

from .book import BookPage
from .item import BookItem


class PageLink(models.Model):
    name = models.TextField()  # Название ссылки
    from_page = models.ForeignKey(BookPage,
                                  on_delete=models.CASCADE)  # Ссылка на исходную страницу
    to_page = models.ForeignKey(BookPage,
                                related_name="to_page",
                                on_delete=models.CASCADE)  # Ссылка на целевую страницу

    items = models.ManyToManyField(BookItem, blank=True)  # требуемые предметы для перехода по ссылке

    class Meta:
        # Уникальность комбинации исходной и целевой страницы для модели PageLink
        unique_together = ["from_page", "to_page"]

    def __str__(self):
        # Строковое представление модели PageLink
        return f"{self.from_page.title} -> {self.to_page.title} ({self.id})"

    def has_all_required(self, required_progress_items):
        # проверяем все ли вещи у нас есть для того, чтобы пройти по ссылке
        return all(item in required_progress_items for item in self.items.all())
