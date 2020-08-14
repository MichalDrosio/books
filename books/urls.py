from django.urls import path

from books.views import show_all_books, show_book_details, add_book, delete_book

app_name = 'books'


urlpatterns = [
    path('', show_all_books, name='all_books'),
    path('books-detail/<int:book_id>/', show_book_details, name='book_details'),
    path('add-book/', add_book, name='add_book'),
    path('delete-book/<int:book_id>/', delete_book, name='delete_book'),


]