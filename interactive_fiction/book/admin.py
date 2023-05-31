from __future__ import annotations

from django.contrib import admin

from .models.book import Book
from .models.book import BookPage
from .models.book import BookProgress
from .models.item import Item
from .models.page import PageLink


class ItemAdminMixin:
    filter_horizontal = ('items',)

    def display_items(self, obj):
        return ', '.join([item.name for item in obj.items.all()])

    display_items.short_description = 'Items'


@admin.register(BookProgress)
class BookProgressAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['user', 'book', 'book_page', 'display_items']


@admin.register(BookPage)
class BookPageAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'book', 'display_items']


@admin.register(PageLink)
class PageLinkAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'from_page', 'to_page', 'display_items']


@admin.site.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'first_page', 'cover_art']


@admin.site.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name']
