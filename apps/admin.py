from django.contrib import admin
from .models import Books, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'title']
    search_fields = ['id', 'author']
