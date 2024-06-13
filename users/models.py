from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {"blank": True, "null": True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE, help_text='введите номер телефона')
    avatar = models.ImageField(upload_to='users/avatars', **NULLABLE, verbose_name='Аватар')
    token = models.CharField(max_length=100, verbose_name='токен', **NULLABLE)
    country = models.CharField(max_length=100, verbose_name='страна', **NULLABLE)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.email
