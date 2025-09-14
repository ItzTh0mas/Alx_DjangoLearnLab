#retrieve.md
Input:
# Retrieve the book by ID
book = Book.objects.get(id=1)

# Display all attributes
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
print(f"ID: {book.id}")

# Alternative: Get all books
all_books = Book.objects.all()
print(f"All books: {all_books}")

# Alternative: Filter by title
book_by_title = Book.objects.filter(title="1984").first()
print(f"Book by title: {book_by_title}")

Output:
Title: 1984
Author: George Orwell
Publication Year: 1949
ID: 1
All books: <QuerySet [<Book: 1984 by George Orwell (1949)>]>
Book by title: 1984 by George Orwell (1949)