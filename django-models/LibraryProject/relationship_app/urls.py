from django import path 

from .import views 
urlpatterns=[
    path("books/",views.get_books,name="get_books"), 
    path("book-detail/<int:pk>/",views.BookDetail.as_view(),name="book_detail")
]

from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.user_register, name='register'),
]
