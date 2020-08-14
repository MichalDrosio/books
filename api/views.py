from rest_framework import generics, filters
from api.serialaizers import BookSerializers
from books.models import Book, Author


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    search_fields = ['published_date', 'authors']
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['published_date']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers