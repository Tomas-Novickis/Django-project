from django.http import JsonResponse
from genre.models import Genre

# Function Based View


def list_of_genres(request):
    genres = Genre.objects.all()
    data = {'genres': list(genres.values())}
    return JsonResponse(data)
