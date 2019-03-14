from django.urls import path
from .api import ListApi, CardApi
from .views import HomeView


urlpatterns = [
    path('lists', ListApi.as_view(), name='board_listapi'),
    path('cards', CardApi.as_view(), name='board_cardapi'),
    path('', HomeView.as_view(), name='board_homeview'),
]
