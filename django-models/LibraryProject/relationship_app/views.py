from .models import Author, Book, Library, Librarian
from django.shortcuts import render
from django.views.generic import DetailView

def get_books(request): 
    books = Book.objects.all()

    context = {
        "books":books
    } 
    return render(request,"relationship_app/list_books.html",context)


class BookDetail(DetailView):
    model=Book