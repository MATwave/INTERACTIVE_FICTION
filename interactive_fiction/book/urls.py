from __future__ import annotations

from django.urls import path

from .views import book
from .views import index

urlpatterns = [
    path("", index),
    path("book/<int:book_id>", book),
]
