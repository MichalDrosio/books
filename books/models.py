from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.


class Author(models.Model):
    authors = models.CharField(max_length=50)

    def __str__(self):
        return self.authors


class Category(models.Model):
    categories = models.CharField(max_length=20)

    def __str__(self):
        return self.categories


class Book(models.Model):
    title = models.CharField(max_length=100)
    average_rating = models.FloatField(default=0)
    ratings_count = models.PositiveIntegerField(default=0)
    published_date = models.CharField(max_length=10)
    thumbnail = models.URLField(("Link"), max_length=128, db_index=True, unique=True, blank=True, null=True,)
    authors = models.ManyToManyField(Author)
    categories = models.ManyToManyField(Category)
    publisher = models.CharField(max_length=500)
    description = models.TextField()
    page_count = models.PositiveIntegerField()


class ValueVotesBook(models.Model):
    BOOK_VALUE_VOTE = [(i, str(i)) for i in range(1, 11)]
    value_vote = models.FloatField(choices=BOOK_VALUE_VOTE, verbose_name='Głos')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)


# class IndustryIdentifiers(models.Model):
#     type = models.CharField(max_length=20)
#     identifier = models.BigIntegerField()
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
