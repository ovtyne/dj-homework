from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    user_key = models.CharField(max_length=50, default=0, verbose_name='ключ пользователя')
    is_active = models.BooleanField(default=False, verbose_name='почта подтверждена')
    phone = models.CharField(max_length=35, verbose_name='телефон', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='аватар', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='страна')

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    