#update.md
# Retrieve the book
book = Book.objects.get(id=1)

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Verify the update
updated_book = Book.objects.get(id=1)
print(f"Updated book: {updated_book}")
print(f"New title: {updated_book.title}")

# Alternative bulk update method:
# Book.objects.filter(id=1).update(title="Nineteen Eighty-Four")

Output:
Updated book: Nineteen Eighty-Four by George Orwell (1949)
New title: Nineteen Eighty-Four