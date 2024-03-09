import json

from asgiref.sync import sync_to_async
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views import View
from game.models import Game
from publisher.forms import PublisherForm
from publisher.models import Publisher


class ListOfPublishers(View):
    def get(self, request):
        publishers = Publisher.objects.all()
        data = {'publishers': list(publishers.values())}
        return JsonResponse(data)


class PublisherById(View):
    def get(self, request, publisher_id):
        publisher = Publisher.objects.filter(id=publisher_id)
        return JsonResponse({'publisher': list(publisher.values())})


class CreatePublisher(View):
    model = Publisher
    form_class = PublisherForm

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            form = PublisherForm(data)
            if form.is_valid():
                publisher = form.save()
                return JsonResponse({
                    'success': f'Publisher by id {publisher.id} is created.'})
        except Exception as error:
            return JsonResponse({'Error': f'{error}.'})


class DeletePublisher(View):
    def get(self, request, publisher_id):
        try:
            publisher = Publisher.objects.get(id=publisher_id)
            publisher.delete()
            return JsonResponse({
                'Publisher by id': f'{publisher_id} is successfully deleted'})
        except ObjectDoesNotExist:
            return JsonResponse({'Publisher by id':
                                 f'{publisher_id} does not exist in database'})


class PublisherGameRating(View):
    def get(self, request, id):
        try:
            sum = 0
            i = 0
            games = Game.objects.filter(publisher__id=id).prefetch_related(
                                                            'rating_set')
            for game in games:
                ratings = game.rating_set.all().values('game_rating')
                for rating in ratings:
                    rating = rating['game_rating']
                    sum += int(rating)
                    i += 1
            avg = sum/i
            return JsonResponse({'Success':
                                f'Average rating by this publisher is {avg}.'})
        except ZeroDivisionError:
            return JsonResponse({
                'Error': 'Games not found by this publisher'}, status=404)


class PublisherUsersAge(View):
    def get(self, request, id):
        try:
            sum = 0
            i = 0
            games = Game.objects.filter(publisher__id=id).prefetch_related(
                                                            'user_set')
            for game in games:
                users = game.user_set.all().values('age')
                for user in users:
                    sum += int(user['age'])
                    i += 1
            avg = sum/i
            return JsonResponse({'Success':
                                f'Average age of users is {avg}.'})
        except ZeroDivisionError:
            return JsonResponse({
                'Error': 'Users is not found'}, status=404)


class AsyncPublisherUsersAge(View):
    async def async_method(self, request, id):
        sync_instance = PublisherUsersAge()
        async_sync_method = sync_to_async(sync_instance.get)
        response_data = await async_sync_method(request, id)
        return response_data

    async def get(self, request, *args, **kwargs):
        response_data = await self.async_method(request, kwargs['id'])
        return response_data


class BulkCreatePublisher(View):
    model = Publisher
    form_class = PublisherForm

    def post(self, request, *args, **kwargs):
        try:
            data_many = json.loads(request.body)
            publishers_data = []
            for data in data_many:
                form = PublisherForm(data)
                if form.is_valid():
                    publishers_data.append(form.cleaned_data)
                else:
                    return JsonResponse({'Validation error': form.errors})
            publishers = Publisher.objects.bulk_create(
                [Publisher(**data) for data in publishers_data])
            return JsonResponse({
                'success': f'Publishers {publishers} are created.'})
        except Exception as error:
            return JsonResponse({'Error': f'{error}.'})
