from django.contrib.auth.models import AbstractUser
from django.db import models


NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватарка', **NULLABLE)
    phone = models.CharField(max_length=30, verbose_name='Номер телефона')
    country = models.CharField(max_length=100, verbose_name='Страна')
    email = models.EmailField(unique=True, verbose_name='email')

    token = models.CharField(max_length=200, verbose_name='токен верификации', **NULLABLE)

    username = None

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.last_name} {self.first_name} ({self.email})'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
