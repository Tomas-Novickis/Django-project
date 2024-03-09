from django.test import Client, TestCase
from django.urls import reverse
from publisher.models import Publisher


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.publisher = Publisher.objects.create(name='TestPublisher')
        self.create_url = reverse('create-publisher')
        self.delete_url = reverse('delete-publisher',
                                  args=[self.publisher.pk])

    def test_create_publisher_post(self):

        new_publisher_data = {
            'name': 'a'
        }

        self.client.post(self.create_url, new_publisher_data,
                         content_type="application/json")
        new_publisher = Publisher.objects.get(name=new_publisher_data['name'])
        self.assertEqual(new_publisher.name, new_publisher_data['name'])

    def test_delete_publisher_get(self):

        before_count = Publisher.objects.count()
        self.client.get(self.delete_url)
        after_count = Publisher.objects.count()
        self.assertEqual(before_count - after_count, 1)
