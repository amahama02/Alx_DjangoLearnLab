from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Book
from django.urls import reverse_lazy
from .forms import BookForm

class BookListView(PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'bookshelf/book_list.html'
    context_object_name = 'books'
    permission_required = 'bookshelf.can_view'
    raise_exception = True

    def get_queryset(self):
        return Book.objects.all()

class BookCreateView(PermissionRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'bookshelf/book_form.html'
    success_url = reverse_lazy('book_list')
    permission_required = 'bookshelf.can_create'
    raise_exception = True