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


class BookProgressAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['user', 'book', 'book_page', 'display_items']


class BookPageAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['title', 'book', 'display_items']


class PageLinkAdmin(ItemAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'from_page', 'to_page', 'display_items']


admin.site.register(Book)
admin.site.register(BookPage, BookPageAdmin)
admin.site.register(PageLink, PageLinkAdmin)
admin.site.register(Item)
admin.site.register(BookProgress, BookProgressAdmin)
