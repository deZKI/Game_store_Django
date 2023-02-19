from django.db import models
from django.db.models import Avg

from users.models import User

# Возрастной ценз взят из Википедии
Russian_system_of_age_ratings = [
    ('Информационная продукция для детей, не достигших возраста шести лет', '0+'),
    ('Информационная продукция для детей, достигших возраста шести лет', '6+'),
    ('Информационная продукция для детей, достигших возраста двенадцати лет', '12+'),
    ('Информационная продукция для детей, достигших возраста шестнадцати лет', '16+'),
    ('Информация, запрещённая для распространения среди детей', '18+'),
]


class GameGenre(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/catalog/genre/{self.slug}'

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Developer(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Имя')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издатель'
        verbose_name_plural = 'Издатели'


class Tag(models.Model):
    """Класс модели тегов. У любого магазина игр есть поиск
        по тегам - то есть по ключевым словам"""
    name = models.CharField("Тег", max_length=50, unique=True)
    slug = models.SlugField("url", max_length=100, unique=True)
    published = models.BooleanField("Отображать?", default=True)

    def get_absolute_url(self):
        return f'/catalog/tag/{self.slug}'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Game(models.Model):
    """Модель для создания игры """
    name = models.CharField(max_length=100, unique=True, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(max_length=300, verbose_name='Описание')
    price = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Цена')
    quantity = models.PositiveIntegerField(default=0, verbose_name='Количество')
    genres = models.ManyToManyField(to=GameGenre, verbose_name='Жанр')
    tags = models.ManyToManyField(to=Tag, verbose_name='Теги', blank=True)
    developer = models.ForeignKey(to=Developer, on_delete=models.PROTECT,
                                  verbose_name='Разработчик')  # запрещает удалять пользователя, пока у него есть посты.
    publisher = models.ForeignKey(to=Publisher, on_delete=models.PROTECT,
                                  verbose_name='Издатель')
    release_date = models.DateField(verbose_name='Дата выхода')
    age_limit = models.CharField(max_length=70, choices=Russian_system_of_age_ratings, verbose_name='Возрастной ценз')

    draft = models.BooleanField(default=True, verbose_name='Готов?')
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/catalog/game/{self.slug}'

    def average_rating(self):
        """Для получения среднего рейтинга игры -> aggregate возвращает словарь"""
        return Rating.objects.filter(game=self).aggregate(Avg("rating"))["rating__avg"] or 0

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"


class Rating(models.Model):
    """Модель для создания рейтинга игры. Связываем пользователя и иргу"""
    user = models.ForeignKey(User, related_name='user_rating', on_delete=models.CASCADE)
    game = models.ForeignKey(Game, related_name='overall_score', on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.game.name}: {self.rating}"


class GameImage(models.Model):
    """Модель для создания картинок игры. Удаляются вместе с игрой"""
    product = models.ForeignKey(
        Game,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField("image")
