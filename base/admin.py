from django.contrib.admin import ModelAdmin, register
from base.models import Book

@register(Book)
class BookAdmin(ModelAdmin):
    list_display = ['title', 'author', 'publisher','price']
