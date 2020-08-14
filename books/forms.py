from django import forms
from multiselectfield import MultiSelectFormField

from books import models
from books.models import ValueVotesBook, Book, Author, Category


class ValueVoteFrom(forms.ModelForm):
    class Meta:
        model = ValueVotesBook
        fields = ('value_vote',)


class AddAuthorForm(forms.CheckboxSelectMultiple):
    class Meta:
        model = Author
        fields = ('authors',)


class AddCategoryForm(forms.CheckboxSelectMultiple):
    class Meta:
        model = Category
        fields = ('categories',)


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ('average_rating', 'ratings_count', 'thumbnail')
        widgets = {'categories': AddCategoryForm, 'authors': AddAuthorForm}


