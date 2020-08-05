from django import forms

from books.models import ValueVotesBook


class ValueVoteFrom(forms.ModelForm):
    class Meta:
        model = ValueVotesBook
        fields = ('value_vote',)