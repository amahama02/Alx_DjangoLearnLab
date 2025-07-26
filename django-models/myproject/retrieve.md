from bookshelf.models import Book
retrieved_book = Book.objects.filter(title="1984").first() # Use .first() to handle duplicates
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Publication Year: {retrieved_book.publication_year}")
print(f"Full object: {retrieved_book}")