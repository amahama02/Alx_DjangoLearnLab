# django-models/LibraryProject/relationship_app/query_samples.py

# This script is meant to be run within the Django shell or with django-extensions' runscript.
# Example usage in Django shell:
# from relationship_app.models import Author, Book, Library, Librarian
# from relationship_app.query_samples import * # This will execute the code below

import os
import django

# Configure Django settings if running as a standalone script (e.g., with python query_samples.py)
# This part is often not needed if run via manage.py shell/runscript, but is good practice for standalone.
# Replace 'LibraryProject.settings' with your actual project's settings module path if different.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

print("--- Sample Data Creation ---")

# Create Authors
author1, created = Author.objects.get_or_create(name="Jane Austen")
author2, created = Author.objects.get_or_create(name="George Orwell")
author3, created = Author.objects.get_or_create(name="Agatha Christie")
print(f"Authors created/retrieved: {author1.name}, {author2.name}, {author3.name}")

# Create Books
book1, created = Book.objects.get_or_create(title="Pride and Prejudice", author=author1)
book2, created = Book.objects.get_or_create(title="1984", author=author2)
book3, created = Book.objects.get_or_create(title="Animal Farm", author=author2)
book4, created = Book.objects.get_or_create(title="Murder on the Orient Express", author=author3)
book5, created = Book.objects.get_or_create(title= "Emma", author=author1)
print(f"Books created/retrieved: {book1.title}, {book2.title}, {book3.title}, {book4.title}, {book5.title}")

# Create Libraries
library1, created = Library.objects.get_or_create(name="Central City Library")
library2, created = Library.objects.get_or_create(name="University Library")
print(f"Libraries created/retrieved: {library1.name}, {library2.name}")

# Add books to libraries (ManyToMany)
library1.books.add(book1, book2, book4)
library2.books.add(book2, book3, book5)
print(f"Books added to {library1.name} and {library2.name}")

# Create Librarians
librarian1, created = Librarian.objects.get_or_create(name="Alice Smith", library=library1)
librarian2, created = Librarian.objects.get_or_create(name="Bob Johnson", library=library2)
print(f"Librarians created/retrieved: {librarian1.name}, {librarian2.name}")


print("\n--- Sample Queries ---")

# Query all books by a specific author.
print("\n1. Query all books by a specific author (George Orwell):")
orwell_books = Book.objects.filter(author__name="George Orwell")
for book in orwell_books:
    print(f"- {book.title}")

# List all books in a library.
print("\n2. List all books in a library (Central City Library):")
central_library = Library.objects.get(name="Central City Library")
for book in central_library.books.all():
    print(f"- {book.title}")

# Retrieve the librarian for a library.
print("\n3. Retrieve the librarian for a library (University Library):")
university_library = Library.objects.get(name="University Library")
# Accessing the librarian via the related_name defined in Librarian model
librarian_for_university = university_library.librarian_profile
if librarian_for_university:
    print(f"- Librarian for {university_library.name}: {librarian_for_university.name}")
else:
    print(f"- No librarian found for {university_library.name}")

print("\n--- End of Queries ---")