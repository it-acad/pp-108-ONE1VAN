from django.urls import path
from .views import *

urlpatterns = [
    path('books_view/', books_view, name='view'),
    path('<int:book_id>/', book_detail, name='book_detail'),
    path('create/', create_book, name='create_book'),
]