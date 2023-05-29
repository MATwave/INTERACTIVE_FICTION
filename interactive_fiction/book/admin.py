from __future__ import annotations

from django.contrib import admin

from .models import Book
from .models import BookPage
from .models import PageLink

admin.site.register(Book)
admin.site.register(BookPage)
admin.site.register(PageLink)
