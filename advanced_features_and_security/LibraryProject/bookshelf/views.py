from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Book

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permission_required = 'bookshelf.can_view'
    raise_exception = True

    def get_queryset(self):
        return Book.objects.all()