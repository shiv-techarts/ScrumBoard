from django.urls import path
from .api import LoginView, LogOutView


urlpatterns = [
    path('login', LoginView.as_view(), name='auth_api_login'),
    path('logout', LogOutView.as_view(), name='auth_api_logout'),
]
