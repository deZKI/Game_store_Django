# Generated by Django 4.1.7 on 2023-02-17 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='realease_date',
            new_name='release_date',
        ),
    ]