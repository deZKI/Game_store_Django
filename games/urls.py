
from django.urls import path
from games.views import GameView, GameListView, JsonFilterGameListView

app_name = 'games'
urlpatterns = [
    path('', GameListView.as_view(), name='catalog'),
    path('json-filter', JsonFilterGameListView.as_view(), name='json_filter'),
    path('game/<slug:game_slug>', GameView.as_view() , name='game'),


    # path('genres/<slug:genre_slug/>', GamesListView.as_view(), name='genres')
    #path('tags/<slug:tag_slug>/', GamesListView.as_view(), name='tags'),

]
