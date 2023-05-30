from __future__ import annotations

from django.contrib import admin

from .models.book import Book
from .models.book import BookPage
from .models.book import BookProgress
from .models.item import Item
from .models.page import PageLink


class BookProgressAdmin(admin.ModelAdmin):
    filter_horizontal = ('items',)


admin.site.register(Book)
admin.site.register(BookPage, BookProgressAdmin)
admin.site.register(PageLink)
admin.site.register(Item)
admin.site.register(BookProgress, BookProgressAdmin)
