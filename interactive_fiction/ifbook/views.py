from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import FormView
from django.views.generic import ListView

from .forms.registration import RegistrationForm
from .models.book import Book
from .models.item import BookItem
from .models.page import BookPage
from .models.progress import BookProgress


class RegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = RegistrationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return super().form_valid(form)


class IndexView(ListView):
    model = Book
    context_object_name = 'books'
    template_name = 'book_index.html'


class BookView(LoginRequiredMixin, View):
    def get(self, request, book_id):
        '''Отрисовка книги'''

        book = get_object_or_404(Book, id=book_id)
        if not book.first_page:
            return render(request, "book.html", context={"book": book})

        progress = BookProgress.reading_progress(user=request.user, book=book)
        if progress is None:
            progress = BookProgress.start_reading(user=request.user, book=book)

        return redirect(reverse("page", kwargs={"book_id": book.id,
                                                "page_id": progress.book_page.id}))


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

        item = get_object_or_404(BookItem, id=item_id)
        progress.items.add(item)

        return redirect(reverse('page', kwargs={'book_id': book_id,
                                                'page_id': page_id}))
