from django import path 

from .import views 
urlpatterns=[
    path("books/",views.get_books,name="get_books"), 
    path("book-detail/<int:pk>/",views.BookDetail.as_view(),name="book_detail")
]