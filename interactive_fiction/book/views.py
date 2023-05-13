from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.shortcuts import render

from .models import Book


# Create your views here.
def index(request):
    return render(request, "book_index.html", context={"books": Book.objects.all()})


def book(request, book_id):
    return render(request, "book.html", context={"book": get_object_or_404(Book, id=book_id)})
