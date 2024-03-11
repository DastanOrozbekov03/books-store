from django.urls import path
from .views import get_books, get_book, create_book, update_book, delete_book

urlpatterns = [
    path('books/', get_books, name='get_books'),
    path('books/<int:pk>/', get_book, name='get_book'),
    path('books/create/', create_book, name='create_book'),
    path('books/update/<int:pk>/', update_book, name='update_book'),
    path('books/delete/<int:pk>/', delete_book, name='delete_book'),
]