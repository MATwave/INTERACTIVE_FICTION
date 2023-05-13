from __future__ import annotations

from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .models import Book
from .models import BookPage


# Create your views here.
def index(request):
    return render(request, "book_index.html", context={"books": Book.objects.all()})


def book(request, book_id):
    b = get_object_or_404(Book, id=book_id)
    if not b.first_page:
        return render(request, "book.html", context={"book": b})
    return redirect(reverse("page", kwargs={"book_id": b.id, "page_id": b.first_page.id}))


def page(request, book_id, page_id):
    return render(request, "page.html", context={"page": get_object_or_404(BookPage, book__id=book_id, id=page_id)})
