from django.db import models

# Create your models here.


class Author(models.Model):
    authors = models.CharField(max_length=50)


class Category(models.Model):
    categories = models.CharField(max_length=50)


class Book(models.Model):
    title = models.CharField(max_length=100)
    average_rating = models.FloatField(default=0)
    ratings_count = models.PositiveIntegerField(default=0)
    published_date = models.DateTimeField()
    thumbnail = models.URLField(("Book Number"), max_length=128, db_index=True, unique=True, blank=True)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)


BOOK_VALUE_VOTE = [(i, str(i)) for i in range(1,11)]


class ValueVotesBook(models.Model):
    value_vote = models.FloatField(choices=BOOK_VALUE_VOTE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
