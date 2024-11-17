 # relationship_app/views.py
from django.shortcuts import render
from .models import Book

def list_books(request):
    books = Book.objects.all()  # Query all book entries
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)


from django.views.generic.detail import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    # Define the model and template to use
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
