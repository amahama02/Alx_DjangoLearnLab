# django-models/LibraryProject/relationship_app/urls.py

from django.urls import path
from . import views # Import views from the current app

urlpatterns = [
    # URL for the function-based view
    # Example: /relationship/books/
    path('books/', views.book_list, name='book_list'),

    # URL for the class-based view (using primary key for detail)
    # Example: /relationship/library/1/ (where 1 is the library's ID)
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]