#create.md
Input:
# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Alternative method:
# book = Book(title="1984", author="George Orwell", publication_year=1949)
# book.save()

print(f"Created book: {book}")
print(f"Book ID: {book.id}")

Output:
Created book: 1984 by George Orwell (1949)
Book ID: 1