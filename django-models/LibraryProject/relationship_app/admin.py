from django.contrib import admin
from .models import Author, Book, Library, Librarian, UserProfile

# Existing registrations
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    search_fields = ('title', 'author__name')
    list_filter = ('author',)

admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(Library)
admin.site.register(Librarian)

# New UserProfile admin
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role')
    list_filter = ('role',)
    search_fields = ('user__username', 'user__email')

admin.site.register(UserProfile, UserProfileAdmin)