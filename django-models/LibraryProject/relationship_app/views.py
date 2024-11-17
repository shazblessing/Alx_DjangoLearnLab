from .models import Book
from .models import Library
from django.shortcuts import render,get_object_or_404
from django.views.generic import DetailView

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