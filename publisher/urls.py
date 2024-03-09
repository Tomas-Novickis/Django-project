from django.urls import path
from publisher.views import (AsyncPublisherUsersAge, BulkCreatePublisher,
                             CreatePublisher, DeletePublisher,
                             ListOfPublishers, PublisherById,
                             PublisherGameRating, PublisherUsersAge)

urlpatterns = [
     # API-endpoint to get list of Publishers
     path('publishers/', ListOfPublishers.as_view(),
          name='list-of-publishers'),
     # API-endpoint to get Publisher by Id
     path('publishers/<int:publisher_id>/', PublisherById.as_view(),
          name='publisher-by-id'),
     #  API-endpoint to create a publisher
     path('publishers/create', CreatePublisher.as_view(),
          name='create-publisher'),
     #  API-endpoint to delete a publisher
     path('publishers/delete/<int:publisher_id>/', DeletePublisher.as_view(),
          name='delete-publisher'),
     # API-endpoint to take publisher_id as a GET parameter
     # and returns AVG rate for every game that the publisher has
     path('publishers/rating/<int:id>/', PublisherGameRating.as_view(),
          name='publisher-game-rating'),
     # API-endpoint to take publisher_id as a GET parameter
     # and returns AVG age of users that play in games that the publisher has.
     path('publishers/users/<int:id>/', PublisherUsersAge.as_view(),
          name='publisher-user-age'),
     # Async version of PublisherUsersAge view
     path('publishers/users/async/<int:id>/', AsyncPublisherUsersAge.as_view(),
          name='publisher-async-game-rating'),
     #  API-endpoint to bulk create a publisher
     path('publishers/bulk/create', BulkCreatePublisher.as_view(),
          name='bulk-create-publisher'),
]
