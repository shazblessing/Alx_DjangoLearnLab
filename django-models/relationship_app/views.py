from django.shortcuts import render
from .models import Book
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books":books})

from .forms import BookForm
from django.views.generic import DetailView
from django.views.generic.detail import DetailView
from .models import Library  # Adjust the model import as needed

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
   from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView

class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to a home page or any appropriate view
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
 