from django.urls import path
from game.views import CreateGame, DeleteGame, GameById, ListOfGames

urlpatterns = [
    # API-endpoint to get list of Games from generic view
    path('games/', ListOfGames.as_view(), name='list-of-games'),
    # API-endpoint to get Game by Id
    path('games/<int:pk>/', GameById.as_view(), name='game-by-id'),
    #  API-endpoint to create a Game
    path('games/create', CreateGame.as_view(), name='create-game'),
    #  API-endpoint to Delete a Game
    path('games/delete/<int:game_id>/', DeleteGame.as_view(),
         name='delete-game'),
]
