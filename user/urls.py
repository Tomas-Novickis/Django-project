from django.urls import path
from user.views import (full_user_id, list_of_users, login_user, logout_user,
                        signup_user, user_by_id)

urlpatterns = [
    # API-endpoint to login user
    path('sign_up/', signup_user, name='signup-user'),
    # API-endpoint to login user
    path('login/', login_user, name='login-user'),
    # API-endpoint to logout user
    path('logout/', logout_user, name='logout-user'),
    # API-endpoint to get list of Users
    path('users/', list_of_users, name='list-of-users'),
    # API-endpoint to get User by Id
    path('users/<int:user_id>/', user_by_id, name='user-by-id'),
    # API-endpoint to return full user info and all games that the user has
    path('user_id/<int:id>/', full_user_id, name='full-user-id'),

]
