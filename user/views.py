import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from game.models import Game
from user.forms import CustomUserCreationForm
from user.models import User

from django_project.decorators import admin_required


def signup_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            form = CustomUserCreationForm(data)
            if form.is_valid():
                user = form.save()
                return JsonResponse({
                    'success': f'user by id {user.id} is created.'})
        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


def login_user(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data['username']
            password = data['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return JsonResponse({'message': 'Login successful'})
            else:
                return JsonResponse({'error': 'Invalid username or password'})

        except KeyError:
            return JsonResponse({'error': 'Invalid JSON data'})
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'})


def logout_user(request):
    logout(request)
    return JsonResponse({'success': 'user is logged out'})


@admin_required
def list_of_users(request):
    users = User.objects.all()
    data = {'users': list(users.values())}
    return JsonResponse(data)


@admin_required
def user_by_id(request, user_id):
    user = User.objects.filter(id=user_id)
    return JsonResponse({'user': list(user.values())})


@login_required(login_url='/admin/login/?next=/admin/')
@admin_required
def full_user_id(request, id):
    user_info = User.objects.get(id=id)
    games = Game.objects.filter(user=id)
    user_dict = {
            "id": user_info.pk,
            "nickname": user_info.nickname,
            "email": user_info.email,
            "age": user_info.age
        }
    user_games = [user_dict, list(games.values())]
    return JsonResponse({'user:': user_games})
