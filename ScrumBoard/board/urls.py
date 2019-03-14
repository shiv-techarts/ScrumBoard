from django.urls import path
from .api import ListApiSet, CardApiSet
from rest_framework.routers import DefaultRouter
from .views import HomeView


router = DefaultRouter()

router.register('lists', ListApiSet)
router.register('cards', CardApiSet)

urlpatterns = [
    path('', HomeView.as_view(), name='board_homeview'),
] + router.urls
