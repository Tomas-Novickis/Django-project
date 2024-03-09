from django import forms
from django.forms import ModelForm
from game.models import Game
from genre.models import Genre
from publisher.models import Publisher


class GameForm(ModelForm):
    genres = forms.ModelMultipleChoiceField(
        queryset=Genre.objects.all()
    )
    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all()
    )

    class Meta:
        model = Game
        fields = ['name', 'price', 'release_date', 'genres', 'publisher']
