# Make sure 'book_to_delete' is defined, or retrieve it again (by its updated title):
# from bookshelf.models import Book
# book_to_delete = Book.objects.filter(title="Nineteen Eighty-Four").first()

book_to_delete.delete()

# Verify deletion
all_books = Book.objects.all()
print(f"Remaining books in the database: {all_books}")