# Make sure 'retrieved_book' is defined from the previous step, or retrieve it again:
# from bookshelf.models import Book
# retrieved_book = Book.objects.filter(title="1984").first()

retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()

# Verify the update
updated_book = Book.objects.get(pk=retrieved_book.pk)
print(f"New Title: {updated_book.title}")