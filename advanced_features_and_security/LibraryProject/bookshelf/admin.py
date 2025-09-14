# bookshelf/admin.py
from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    # Display these fields in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality
    search_fields = ('title', 'author')

    # Add filter options in the sidebar
    list_filter = ('publication_year', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
