from django.db import models
from genre.models import Genre
from publisher.models import Publisher


class Game(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    release_date = models.DateField()
    genres = models.ManyToManyField(Genre)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
