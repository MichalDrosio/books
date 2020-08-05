from django.urls import path

from books.views import show_all_books, show_book_details

app_name = 'books'


urlpatterns = [
    path('', show_all_books, name='all_books'),
    path('books-detail/<int:book_id>/', show_book_details, name='book_details'),
]