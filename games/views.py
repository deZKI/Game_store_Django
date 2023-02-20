from django.db.models import Q
from django.http import JsonResponse
from django.views.generic import ListView, DetailView

from common.views import CommonContextMixin
from games.models import Game, GameGenre, Tag


class IndexView(CommonContextMixin, ListView):
    template_name = 'games/index.html'
    title = 'Главная страницы'


class GameListView(CommonContextMixin, ListView):
    """Получение неотфильтрованного(светлого) списка"""
    # https://morioh.com/p/13fad7aa6083
    model = Game
    title = 'Каталог'
    template_name = 'games/catalog.html'
    paginate_by = 10

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data()
        context['genres'] = GameGenre.objects.all()
        context['tags'] = Tag.objects.all()
        return context


class JsonGameView(DetailView):
    """Класс для ajax получение quickview по игры"""


class JsonFilterGameListView(ListView):
    """Класс для ajax получение списка игр по категориям"""

    def get_queryset(self):
        if 'genre' not in self.request.GET.keys():
            queryset = Game.objects.filter(Q(tags__slug__in=self.request.GET.getlist('tag')))
        elif 'tag' not in self.request.GET.keys():
            queryset = Game.objects.filter(Q(genres__slug__in=self.request.GET.getlist('genre')))
        else:
            queryset = Game.objects.filter(
                Q(genres__slug__in=self.request.GET.getlist('genre')),
                Q(tags__slug__in=self.request.GET.getlist('tag'))
            )
        queryset = queryset.distinct('pk').values('name', 'price', 'images__image', 'slug')
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({"games": queryset}, safe=False)


class GameView(CommonContextMixin, DetailView):
    """Для отображения информации об определенной игре"""
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'
    queryset = Game.objects.select_related('developer', 'publisher').prefetch_related('images')
    # Использование prefetch_related необходимо, чтобы дважды не обращаться в базу за фото

# Create your views here.
