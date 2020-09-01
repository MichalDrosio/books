from django.test import TestCase
from django.urls import reverse

from books.models import ValueVotesBook, Book, Author
from books.views import show_all_books
# Create your tests here.


class AuthorTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        print('setUpTestData: Run once to set up non-modified data for all class methods')
        Author.objects.create(authors='tolkien')

    def test_authors(self):
        author = Author.objects.get(id=1)
        field_label = author._meta.get_field('authors').verbose_name
        self.assertEqual(field_label, 'authors')

    def test_authors_max_length(self):
        author = Author.objects.get(id=1)
        max_length = author._meta.get_field('authors').max_length
        self.assertEqual(max_length, 50)


class BookTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='hobbit', description='ja', average_rating=10, page_count=200, ratings_count=10,
                            published_date='2000-01-01', publisher='helion', thumbnail='https://www.youtube.com/?hl=pl&gl=PL',
                            )

    def test_title(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('description').verbose_name
        self.assertEqual(field_label, 'description')

    def test_object(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title}, {book.description}'
        self.assertEquals(expected_object_name, f'{book.title}, {book.description}')
