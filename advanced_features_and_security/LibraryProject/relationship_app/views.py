# django-models/LibraryProject/relationship_app/views.py

from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView # Import for Class-Based Views
from .models import Book, Library, Author # Import your models

# --- Function-based View ---
def book_list(request):
    """
    Lists all books stored in the database.
    """
    books = Book.objects.all().select_related('author') # Optimize query by selecting related author data
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)

# --- Class-based View ---
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library, listing all books available in that library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library' # The name of the context variable for the object

    # You can optionally override get_queryset to prefetch related books if needed for complex scenarios
    # def get_queryset(self):
    #     return super().get_queryset().prefetch_related('books')