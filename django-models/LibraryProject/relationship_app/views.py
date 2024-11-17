from .models import Book
from .models import Library
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required


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
    
    def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')  # Replace 'home' with your preferred route
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})