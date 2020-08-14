from rest_framework import serializers
from books.models import Book


class BookSerializers(serializers.ModelSerializer):
    authors = serializers.SlugRelatedField(many=True, read_only=True, slug_field='authors')
    categories = serializers.SlugRelatedField(many=True, read_only=True, slug_field='categories')

    class Meta:
        model = Book
        fields = ('title', 'authors', 'published_date', 'categories', 'average_rating', 'ratings_count', 'thumbnail')