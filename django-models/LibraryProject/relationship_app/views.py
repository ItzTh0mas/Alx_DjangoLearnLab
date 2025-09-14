from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import DetailView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from django.utils.decorators import method_decorator
from .models import Book, Library, UserProfile

# Existing views
@login_required
def list_books(request):
    """Function-based view to list all books"""
    books = Book.objects.all()  # type: ignore
    return render(request, 'relationship_app/list_books.html', {'books': books})

@method_decorator(login_required, name='dispatch')
class LibraryDetailView(DetailView):
    """Class-based view to display library details"""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# Role checking functions
def is_admin(user):
    """Check if user has Admin role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    """Check if user has Librarian role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    """Check if user has Member role"""
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Role-based views
@user_passes_test(is_admin)
def admin_view(request):
    """Admin-only view"""
    # Get all users and their profiles for admin dashboard
    users = UserProfile.objects.select_related('user').all()  # type: ignore
    books = Book.objects.all()  # type: ignore
    libraries = Library.objects.all()  # type: ignore
    
    context = {
        'users': users,
        'total_books': books.count(),
        'total_libraries': libraries.count(),
        'user_role': request.user.userprofile.role,
    }
    return render(request, 'relationship_app/admin_view.html', context)

@user_passes_test(is_librarian)
def librarian_view(request):
    """Librarian-only view"""
    books = Book.objects.all()  # type: ignore
    libraries = Library.objects.all()  # type: ignore
    
    context = {
        'books': books,
        'libraries': libraries,
        'user_role': request.user.userprofile.role,
    }
    return render(request, 'relationship_app/librarian_view.html', context)

@user_passes_test(is_member)
def member_view(request):
    """Member-only view"""
    books = Book.objects.all()  # type: ignore
    libraries = Library.objects.all()  # type: ignore
    
    context = {
        'books': books,
        'libraries': libraries,
        'user_role': request.user.userprofile.role,
    }
    return render(request, 'relationship_app/member_view.html', context)