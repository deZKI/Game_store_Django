from django.views.generic import ListView, DetailView

from common.views import CommonContextMixin
from games.models import Game, GameGenre, Tag
from django.core.paginator import Paginator
from django.db.models import Q


class IndexView(CommonContextMixin, ListView):
    template_name = 'games/index.html'
    title = 'Главная страницы'


class GameListView(CommonContextMixin, ListView):
    #https://morioh.com/p/13fad7aa6083
    model = Game
    title = 'Каталог'
    template_name = 'games/catalog.html'
    paginate_by = 1
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data()
        context['genres'] = GameGenre.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class GameView(CommonContextMixin, DetailView):
    """Для отображения информации об определенной игре"""
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'
    queryset = Game.objects.select_related('developer', 'publisher').prefetch_related('images')
    #Использование prefetch_related необходимо, чтобы дважды не обращаться в базу за фото

# Create your views here.
