from __future__ import annotations

from django.urls import path

from .views import index

urlpatterns = [
    path("", index),
]
