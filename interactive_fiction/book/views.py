from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from .models.book import Book
from .models.book import BookPage
from .models.book import BookProgress
from .models.item import Item


class IndexView(View):
    def get(self, request):
        '''Отрисовка главной страницы'''
        return render(request, "book_index.html", context={"books": Book.objects.all()})


class BookView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        '''Отрисовка книги'''
        b = get_object_or_404(Book, id=book_id)
        if not b.first_page:
            return render(request, "book.html", context={"book": b})

        progress = BookProgress.reading_progress(user=request.user, book=b)
        if progress is None:
            progress = BookProgress.start_reading(user=request.user, book=b)

        return redirect(reverse("page", kwargs={"book_id": b.id, "page_id": progress.book_page.id}))


class PageView(LoginRequiredMixin, View):
    def get(self, request, book_id, page_id):
        '''Отрисовка страницы'''
        progress = BookProgress.reading_progress(user=request.user, book=book_id)
        if progress is None:
            return redirect(reverse("book", kwargs={"book_id": book_id}))

        page = get_object_or_404(BookPage, book__id=book_id, id=page_id)
        progress.save_progress(page_id=page)

        links = [
            (link, link.has_all_required(list(progress.items.all()))) for link in page.pagelink_set.all()
        ]
        print(links)

        return render(request,
                      "page.html",
                      context={"page": get_object_or_404(BookPage, book__id=book_id, id=page_id),
                               "items": progress.items.all(),
                               "page_items": page.items.exclude(id__in=progress.items.only('id')),
                               "links": links
                               })


class TakeView(LoginRequiredMixin, View):
    def get(self, request, book_id, page_id, item_id):
        progress = BookProgress.reading_progress(user=request.user, book=book_id)
        if progress is None:
            return redirect(reverse("book", kwargs={"book_id": book_id}))

        item = get_object_or_404(Item, id=item_id)
        progress.items.add(item)

        return redirect(reverse('page', kwargs={'book_id': book_id,
                                                'page_id': page_id}))
