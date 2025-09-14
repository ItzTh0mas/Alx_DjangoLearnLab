# Complete CRUD Operations Script
# Run this in Django shell: python manage.py shell

from bookshelf.models import Book

print("=== CREATE OPERATION ===")
# Create a new book
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)
print(f"Created: {book}")
print(f"Book ID: {book.id}")

print("\n=== RETRIEVE OPERATION ===")
# Retrieve the book
retrieved_book = Book.objects.get(id=book.id)
print(f"Retrieved: {retrieved_book}")
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Year: {retrieved_book.publication_year}")

# Show all books
all_books = Book.objects.all()
print(f"All books: {list(all_books)}")

print("\n=== UPDATE OPERATION ===")
# Update the title
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(f"Updated: {retrieved_book}")

print("\n=== DELETE OPERATION ===")
# Delete the book
book_id = retrieved_book.id
retrieved_book.delete()
print(f"Deleted book with ID: {book_id}")

# Confirm deletion
remaining_books = Book.objects.all()
print(f"Remaining books: {list(remaining_books)}")
print(f"Count: {remaining_books.count()}")