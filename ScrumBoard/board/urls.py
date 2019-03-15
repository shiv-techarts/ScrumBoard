from django.urls import path
from .api import ListApiSet, CardApiSet
from rest_framework.routers import DefaultRouter
from .views import HomeView
from django.views.decorators.csrf import ensure_csrf_cookie


router = DefaultRouter()

router.register('lists', ListApiSet)
router.register('cards', CardApiSet)

urlpatterns = [
    path('', ensure_csrf_cookie(HomeView.as_view()), name='board_homeview'),
] + router.urls
