from api_drf.views import GameViewSet, PublisherViewSet, UserViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'games', GameViewSet)
router.register(r'publishers', PublisherViewSet)
router.register(r'users', UserViewSet, basename='user')

urlpatterns = router.urls
