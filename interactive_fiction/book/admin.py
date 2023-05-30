from __future__ import annotations

from django.contrib import admin

from .models.book import Book
from .models.book import BookPage
from .models. page import PageLink

admin.site.register(Book)
admin.site.register(BookPage)
admin.site.register(PageLink)
