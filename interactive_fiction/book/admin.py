from __future__ import annotations

from django.contrib import admin

from .models import Book
from .models import BookPage


admin.site.register(Book)
admin.site.register(BookPage)
