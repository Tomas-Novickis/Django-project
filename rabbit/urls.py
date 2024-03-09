from django.urls import path
from rabbit.producer import PublisherView

urlpatterns = [
    path('', PublisherView.as_view(), name='rabbit-producer'),
]