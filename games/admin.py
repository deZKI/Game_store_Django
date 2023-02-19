from django.contrib import admin
from image_uploader_widget.admin import ImageUploaderInline

from games.models import GameGenre, Game, GameImage, Developer, Publisher, Tag

# мб выделить в отдельный файл такие настройки или в settings
admin.AdminSite.site_header = 'Бизнес'


class GameImageAdmin(ImageUploaderInline):
    """Использование сторонней библиотеки для
        добавления нескольких фотографий за раз"""
    model = GameImage


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(GameGenre)
class GameGenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'quantity', 'developer', 'publisher', 'average_rating', 'draft']
    readonly_fields = ['average_rating']
    fields = [('name', 'slug', 'average_rating'),
              ('price', 'quantity', 'draft'),
              ('developer', 'publisher', 'release_date'),
              ('description'),
              ('genres', 'tags', 'age_limit'),
              ]
    autocomplete_fields = ["genres", "tags"]
    filter = ['average_rating']
    prepopulated_fields = {'slug': ('name', )}
    inlines = [
        GameImageAdmin,
    ]

# Register your models here.
