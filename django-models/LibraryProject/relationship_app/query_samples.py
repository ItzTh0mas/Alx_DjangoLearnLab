# relationship_app/query_samples.py
"""
Sample queries demonstrating Django ORM relationships
Run this script using: python manage.py shell < relationship_app/query_samples.py
Or copy and paste in Django shell: python manage.py shell
"""

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample data for testing queries"""
    print("Creating sample data...")

    # Create authors
    author1 = Author.objects.create(name="J.K. Rowling")# type: ignore
    author2 = Author.objects.create(name="George Orwell")# type: ignore
    author3 = Author.objects.create(name="Harper Lee")# type: ignore

    # Create books
    book1 = Book.objects.create(title="Harry Potter and the Philosopher's Stone", author=author1)# type: ignore
    book2 = Book.objects.create(title="Harry Potter and the Chamber of Secrets", author=author1)# type: ignore
    book3 = Book.objects.create(title="1984", author=author2)# type: ignore
    book4 = Book.objects.create(title="Animal Farm", author=author2)# type: ignore
    book5 = Book.objects.create(title="To Kill a Mockingbird", author=author3)# type: ignore

    # Create libraries
    library1 = Library.objects.create(name="Central Public Library")# type: ignore
    library2 = Library.objects.create(name="University Library")# type: ignore

    # Add books to libraries (ManyToMany relationship)
    library1.books.add(book1, book2, book3, book5)
    library2.books.add(book3, book4, book5)

    # Create librarians
    librarian1 = Librarian.objects.create(name="Alice Johnson", library=library1)# type: ignore
    librarian2 = Librarian.objects.create(name="Bob Smith", library=library2)# type: ignore

    print("Sample data created successfully!")

def query_books_by_author():
    """Query all books by a specific author (ForeignKey relationship)"""
    print("\n=== QUERY 1: Books by a specific author ===")

    # Find author
    author_name = "George Orwell"
    try:
        author = Author.objects.get(name=author_name)# type: ignore
        # Query books by this author using ForeignKey relationship
        books = Book.objects.filter(author=author)# type: ignore

        print(f"Books by {author_name}:")
        for book in books:
            print(f"  - {book.title}")

        # Alternative method using reverse relationship
        books_reverse = author.book_set.all()
        print(f"\nUsing reverse relationship:")
        for book in books_reverse:
            print(f"  - {book.title}")

    except Author.DoesNotExist: # type: ignore
        print(f"Author '{author_name}' not found")

def query_books_in_library():
    """List all books in a library (ManyToMany relationship)"""
    print("\n=== QUERY 2: Books in a specific library ===")

    library_name = "Central Public Library"
    try:
        library = Library.objects.get(name=library_name)# type: ignore
        # Query books in this library using ManyToMany relationship
        books = library.books.all()

        print(f"Books in {library_name}:")
        for book in books:
            print(f"  - {book.title} by {book.author.name}")

        print(f"\nTotal books: {books.count()}")

    except Library.DoesNotExist:# type: ignore
        print(f"Library '{library_name}' not found")

def query_librarian_for_library():
    """Retrieve the librarian for a library (OneToOne relationship)"""
    print("\n=== QUERY 3: Librarian for a specific library ===")

    library_name = "University Library"
    try:
        library = Library.objects.get(name=library_name)# type: ignore
        # Query librarian using OneToOne relationship
        librarian = library.librarian

        print(f"Librarian for {library_name}: {librarian.name}")

        # Alternative approach
        librarian_alt = Librarian.objects.get(library=library)# type: ignore
        print(f"Alternative query result: {librarian_alt.name}")

    except Library.DoesNotExist:# type: ignore
        print(f"Library '{library_name}' not found")
    except Librarian.DoesNotExist:# type: ignore
        print(f"No librarian found for {library_name}")

def run_all_queries():
    """Run all sample queries"""
    print("Django ORM Relationship Queries Demo")
    print("=" * 50)

    # Create sample data (comment out if data already exists)
    create_sample_data()

    # Run queries
    query_books_by_author()
    query_books_in_library()
    query_librarian_for_library()

    print("\n" + "=" * 50)
    print("All queries completed!")

# Run all queries when script is executed
if __name__ == "__main__":
    run_all_queries()
