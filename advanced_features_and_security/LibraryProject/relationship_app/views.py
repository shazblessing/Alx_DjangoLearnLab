from .models import Book
from .models import Library
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.views.generic.detail import DetailView  # Correctly add import here
from .models import Library



def get_books(request): 
    books = Book.objects.all()

    context = {
        "books":books
    } 
    return render(request,"relationship_app/list_books.html",context)


class BookDetail(DetailView):
    model=Library
    template_name= "relationship_app/library_detail.html"
    context_object_name="books"

    def get_queryset(self):
        library= get_object_or_404(Book,book=self.kwargs.get("book"))
        return Library.objects.get(library=library)
    
    
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

# Role check function to check for 'Admin' role
def is_admin(user):
    # Ensure the user has a profile and that the role is 'Admin'
    return user.userprofile.role == 'Admin'

# Admin view, accessible only to users with 'Admin' role
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    # Logic for adding a book
    return render(request, 'relationship_app/add_book.html')

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for editing a book
    return render(request, 'relationship_app/edit_book.html', {'book': book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    # Logic for deleting a book
    return redirect('book_list')
