from .models import Book, Library
from django.urls import path
from . import views
from .views import LibraryDetailView
from .views import list_books
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('book/', views.viewmodel,name = 'bookd' ),
    path('library/', LibraryDetailView.as_view(), name = 'list' ),
    path('register/', views.register),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
   

    path('profile/', views.ProfileView.as_view(), name = 'profile'),
    path('admin/', views.admin_view, name = 'admin_view'),
    path('librarian/', views.librarian_view, name = 'librarian_view'),
    path('member/', views.member_view, name = 'member_view'),
    path('add_book/', views.add_book, name = 'add_book'),
    path('edit_book/', views.edit_book, name = 'edit_book'),
    path('delete_book/', views.delete_book, name='delete_book'),
]