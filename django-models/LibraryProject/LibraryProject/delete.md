#delete.md
Input:
# Retrieve the book
book = Book.objects.get(id=1)

# Delete the book
book.delete()

# Confirm deletion by checking all books
all_books = Book.objects.all()
print(f"All books after deletion: {all_books}")
print(f"Number of books: {all_books.count()}")

# Try to retrieve the deleted book (should raise an exception)
try:
    deleted_book = Book.objects.get(id=1)
    print(f"Book still exists: {deleted_book}")
except Book.DoesNotExist:
    print("Book successfully deleted - DoesNotExist exception raised")


Output:
All books after deletion: <QuerySet []>
Number of books: 0
Book successfully deleted - DoesNotExist exception raised
