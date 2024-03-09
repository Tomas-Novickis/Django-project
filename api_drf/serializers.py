from game.models import Game
from publisher.models import Publisher
from rest_framework import serializers
from user.models import User


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = ['name', 'price', 'release_date', 'genres', 'publisher']


class PublisherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Publisher
        fields = ['name']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'nickname', 'email', 'games']


class UserSerializerFull(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'email', 'games']
