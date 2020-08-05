from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render, redirect

# Create your views here.
from books.forms import ValueVoteFrom
from books.models import Book, ValueVotesBook


def show_all_books(request):
    search_query = request.GET.get('Szukaj', '')
    if search_query:
        books = Book.objects.filter(Q(title__icontains=search_query) | Q(authors__authors__icontains=search_query))
    else:
        books = Book.objects.all()
    return render(request, 'books/books_list.html', {'books': books})


def show_book_details(request, book_id):
    book = Book.objects.get(pk=book_id)
    authors = book.authors.all()
    categories = book.categories.all()
    votes = ValueVotesBook.objects.filter(book_id=book)
    if request.method == "POST":
        form = ValueVoteFrom(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.book = book
            new_form.save()
            number_of_votes = 0
            sum_votes = 0
            for vote in votes:
                number_of_votes += 1
            book.ratings_count = number_of_votes
            for value in votes:
                sum_votes += value.value_vote
            average = sum_votes / number_of_votes
            book.average_rating = average
            book.save()
            return redirect('books:book_details', book_id)
    else:
        form = ValueVoteFrom()
    return render(request, 'books/book_details.html', {'book': book, 'authors': authors, 'categories': categories,
                                                       'form': form})

