from django.db.models import Q
from django.views.generic import ListView, DetailView
from Game_store_Django.settings import PAGE_SIZE

from common.views import CommonContextMixin
from games.models import Game, GameGenre, Tag


class IndexView(CommonContextMixin, ListView):
    template_name = 'games/index.html'
    title = 'Главная страница'
    model = Game

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(IndexView, self).get_context_data()
        # context['games_featured'] = Game.objects.filter()
        context['games_recently_released_slider'] = Game.objects.order_by("-id")[:3]
        context['games_recently_released_row'] = Game.objects.order_by("-id")[3:8]
        return context


class GameListView(CommonContextMixin, ListView):
    """Получение нефильтрованного(светлого) списка"""
    # https://morioh.com/p/13fad7aa6083
    model = Game
    # queryset = Game.objects.filter(ready=True)
    title = 'Каталог'
    template_name = 'games/catalog.html'
    paginate_by = PAGE_SIZE

    def get_queryset(self):
        queryset = super(GameListView, self).get_queryset()
        if 'genre' not in self.request.GET.keys() and 'tag' not in self.request.GET.keys():
            return queryset.distinct('pk').only('name', 'price', 'main_image', 'slug')
        elif 'tag' not in self.request.GET.keys():
            queryset = Game.objects.filter(Q(genres__slug__in=self.request.GET.getlist('genre')))
        if 'genre' not in self.request.GET.keys():
            queryset = Game.objects.filter(Q(tags__slug__in=self.request.GET.getlist('tag')))
        queryset = queryset.distinct('pk').only('name', 'price', 'main_image', 'slug')
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GameListView, self).get_context_data()
        context['genres'] = GameGenre.objects.all().values('name', 'slug')
        context['tags'] = Tag.objects.all().values('name', 'slug')
        return context


class ModalGameView(DetailView):
    """Класс для ajax получение quickview по игры"""
    template_name = 'games/product-quick-view.html'
    slug_url_kwarg = 'game_slug'
    queryset = Game.objects.select_related('developer', 'publisher').prefetch_related('images')


class GameView(CommonContextMixin, DetailView):
    """Для отображения информации об определенной игре"""
    template_name = 'games/game.html'
    slug_url_kwarg = 'game_slug'
    model = Game
    queryset = Game.objects.select_related('developer', 'publisher'). \
        only('name', 'description',
             'release_date',
             'quantity',
             'price',
             'age_limit',
             'developer__name', 'publisher__name', 'main_image'
             ).prefetch_related('images')

    def get_object(self, queryset=None):
        self.title = self.kwargs.get('name')
        return super(GameView, self).get_object()

    def get_context_data(self, **kwargs):
        context = super(CommonContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.object.name
        return context

    # Использование prefetch_related необходимо, чтобы дважды не обращаться в базу за фото(у нас там карусель)

# Create your views here.
