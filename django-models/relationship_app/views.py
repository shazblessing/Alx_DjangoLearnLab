from .models import Author, Book, Library, Librarian
from django.shortcuts import render
from django.views.generic import DetailView

def get_books(request): 
    books = Book.objects.all()

    context = {
        "books":books
    } 
    return render(request,"book/book.html",context)


class BookDetail(DetailView):
    model=Book