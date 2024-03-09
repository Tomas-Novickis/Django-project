import json

from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.views.generic import CreateView, DeleteView, DetailView, ListView
from game.forms import GameForm
from game.models import Game


class ListOfGames(ListView):
    model = Game

    def render_to_response(self, context, **response_kwargs):
        games = list(self.get_queryset().values())
        return JsonResponse({'games': games})


class GameById(DetailView):
    model = Game

    def render_to_response(self, context, **kwargs):
        game_id = self.kwargs['pk']
        game = Game.objects.filter(id=game_id)
        data = {'games': list(game.values())}
        return JsonResponse(data)


class CreateGame(CreateView):
    model = Game
    form_class = GameForm

    def post(self, request, *args, **kwargs):
        try:
            data = json.loads(request.body)
            form = GameForm(data)
            if form.is_valid():
                game = form.save()
                return JsonResponse({
                    'success': f'Game by id {game.id} is created.'})

            else:
                return JsonResponse({'Validation error': form.errors})
        except Exception as error:
            return JsonResponse({'Error': f'{error}.'})


class DeleteGame(DeleteView):
    model = Game

    def get(self, request, game_id):
        try:
            game = Game.objects.get(id=game_id)
            game.delete()
        except ObjectDoesNotExist:
            return JsonResponse({
                'Game by id': f'{game_id} does not exist in database'})
        return JsonResponse({
            'Game by id': f'{game_id} is successfully deleted'})
