from django.urls import path
from genre.views import list_of_genres

urlpatterns = [
    path('genres/', list_of_genres, name='list-of-genres'),
]
