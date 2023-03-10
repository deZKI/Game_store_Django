from django.urls import path, include
from api.views import GameListAPIView

from rest_framework import routers

app_name = 'api'


urlpatterns = [
    path('game_list/', GameListAPIView.as_view(), name='get_games'),
]