from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView

from api.services import GamePagination, GameFilter
from games.models import Game
from games.serializers import GameSerializer


class GameListAPIView(ListAPIView):
    queryset = Game.objects.all().distinct('id')
    serializer_class = GameSerializer
    pagination_class = GamePagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = GameFilter




