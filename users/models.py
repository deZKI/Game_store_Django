from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    image = models.ImageField(upload_to='users_images', null=True, blank=True, verbose_name='Аватарка')
    is_verified_email = models.BooleanField(default=False, verbose_name='Подтверждена почта')
    email = models.EmailField(blank=True, verbose_name='Адрес электронной почты', unique=True)


