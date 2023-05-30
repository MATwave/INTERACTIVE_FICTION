from __future__ import annotations

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse

from .models.book import Book
from .models.book import BookPage
from .models.book import BookProgress


def index(request):
    '''Отрисовка главной страницы'''
    return render(request, "book_index.html", context={"books": Book.objects.all()})


@login_required
def book(request, book_id):
    '''Отрисовка книги'''
    b = get_object_or_404(Book, id=book_id)
    if not b.first_page:
        return render(request, "book.html", context={"book": b})

    progress = BookProgress.reading_progress(user=request.user, book=b)

    return redirect(reverse("page", kwargs={"book_id": b.id, "page_id": progress.book_page.id}))


@login_required
def page(request, book_id, page_id):
    '''Отрисовка страницы'''

    BookProgress.save_progress(book_id=book_id, user=request.user, page_id=page_id)

    return render(request, "page.html", context={"page": get_object_or_404(BookPage, book__id=book_id, id=page_id)})
