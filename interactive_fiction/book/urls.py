from __future__ import annotations

from django.urls import path

from .views import book
from .views import index
from .views import page

urlpatterns = [
    path("", index),
    path("book/<int:book_id>", book, name="book"),
    path("book/<int:book_id>/page/<int:page_id>", page, name="page"),
]
