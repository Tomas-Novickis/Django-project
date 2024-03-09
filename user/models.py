from django.contrib.auth.models import AbstractUser
from django.db import models
from game.models import Game


class User(AbstractUser):
    nickname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    games = models.ManyToManyField(Game)

    def __str__(self):
        return self.nickname


class Rating(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_rating = models.CharField(choices=((str(x), x) for x in range(1, 11)))
