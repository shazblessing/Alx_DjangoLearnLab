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
    
   #@user_passes_test(lambda u: u.userprofile.role == 'Admin')
#def admin_view(request):

from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from .models import UserProfile
def has_role(user, role):
    return UserProfile.objects.filter(user=user.id, role=role).exists()
def is_admin(user):
    return getattr(user, 'userprofile', None) and user.userprofile.role == 'Admin'
    return has_role(user, "Admin")
def is_librarian(user):
    return has_role(user, "Librarian")
def is_member(user):
    return has_role(user, "Member")

# Views for Admin users
@user_passes_test(is_admin)
def Admin_view(request):
    # Your view logic here
    return render(request, 'admin_dashboard.html')
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view that only users with the 'Librarian' role can access
@user_passes_test(lambda u: u.userprofile.role == 'Librarian')
# View for Librarian users
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'librarian_view.html')
# Member view that only users with the 'Member' role can access
@user_passes_test(lambda u: u.userprofile.role == 'Member')
    return render(request, 'relationship_app/librarian_view.html')
# View for Member users
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'member_view.html')
    return render(request, 'relationship_app/member_view.html')
