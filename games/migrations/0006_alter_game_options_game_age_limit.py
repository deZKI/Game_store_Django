# Generated by Django 4.1.7 on 2023-02-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_remove_tag_games_game_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'verbose_name': 'Игра', 'verbose_name_plural': 'Игры'},
        ),
        migrations.AddField(
            model_name='game',
            name='age_limit',
            field=models.CharField(choices=[('0+', 'Информационная продукция для детей, не достигших возраста шести лет'), ('6+', 'Информационная продукция для детей, достигших возраста шести лет'), ('12+', 'Информационная продукция для детей, достигших возраста двенадцати лет'), ('16+', 'Информационная продукция для детей, достигших возраста шестнадцати лет'), ('18+', 'Информация, запрещённая для распространения среди детей')], default='0+', max_length=3),
            preserve_default=False,
        ),
    ]