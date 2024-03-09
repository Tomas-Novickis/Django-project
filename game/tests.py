from django.test import Client, TestCase
from django.urls import reverse
from game.models import Game
from genre.models import Genre
from publisher.models import Publisher


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.publisher = Publisher.objects.create(name='TestPublisher')
        self.genre = Genre.objects.create(name="TestGenre")
        self.game = Game.objects.create(name="TestGame",
                                        price=5,
                                        release_date="2022-12-05",
                                        publisher=self.publisher)
        self.game.genres.add(self.genre)
        self.create_url = reverse('create-game')
        self.delete_url = reverse('delete-game', args=[self.game.pk])

    def test_create_game_post(self):
        new_game_data = {
            "name": "TestGame",
            "price": 15,
            "release_date": "2022-12-05",
            "genres": 1,
            "publisher": 8
        }
        self.client.post(self.create_url, new_game_data,
                         content_type="application/json")
        new_game = Game.objects.get(name=new_game_data['name'])
        self.assertEqual(new_game.name, new_game_data['name'])

    def test_delete_game_get(self):

        before_count = Game.objects.count()
        self.client.get(self.delete_url)
        after_count = Game.objects.count()
        self.assertEqual(before_count - after_count, 1)
