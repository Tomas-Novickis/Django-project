from api_drf.serializers import (GameSerializer, PublisherSerializer,
                                 UserSerializer, UserSerializerFull)
from django.shortcuts import get_object_or_404
from game.models import Game
from publisher.models import Publisher
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from user.models import User


class GameViewSet(ViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        game = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(game)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        game = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(game)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        game = get_object_or_404(self.queryset, pk=pk)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PublisherViewSet(ViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        publisher = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(publisher)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        publisher = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(publisher)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        publisher = get_object_or_404(self.queryset, pk=pk)
        publisher.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserViewSet(ViewSet):
    queryset = User.objects.all()
    serializer_class_no_pass = UserSerializer
    serializer_class = UserSerializerFull

    def list(self, request):
        serializer = self.serializer_class_no_pass(self.queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class_no_pass(user)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
