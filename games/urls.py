from django.urls import path

from games.views import GameView, GameListView, ModalGameView
from games.scrapping import parsing


app_name = 'games'
urlpatterns = [
    path('', GameListView.as_view(), name='catalog'),
    path('dump_games/', parsing),

    path('modal-game/<slug:game_slug>',ModalGameView.as_view(), name='modal_game_view'),
    path('game/<slug:game_slug>', GameView.as_view() , name='game'),


    # path('genres/<slug:genre_slug/>', GamesListView.as_view(), name='genres')
    #path('tags/<slug:tag_slug>/', GamesListView.as_view(), name='tags'),

]
