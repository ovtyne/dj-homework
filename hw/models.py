from django.conf import settings
from django.db import models

from users.models import User

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')                              # наименование,
    description = models.TextField(verbose_name='описание', max_length=100)                                            # описание,
    image = models.ImageField(**NULLABLE)                                                              # изображение,
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')    # категория,
    price = models.FloatField(verbose_name='цена')                          # цена за покупку,
    creation_date = models.DateField(verbose_name='дата создания', auto_now_add=True)          # дата создания,
    change_date = models.DateField(verbose_name='дата изменения', auto_now=True)           # дата последнего изменения.
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='владелец')

    def __str__(self):
        return f'Название: {self.title} Категория: {self.category} Цена:{self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('title', 'category', 'price',)


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')   # наименование,
    description = models.TextField(verbose_name='описание')                 # описание.

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('title',)


class Version(models.Model):
    product_ref = models.ForeignKey(to=Product, on_delete=models.CASCADE, default=None, verbose_name='продукт')
    number = models.FloatField(default=0, verbose_name='номер версии')
    name = models.CharField(max_length=150, **NULLABLE, verbose_name='название версии')
    is_current = models.BooleanField(default=False, verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.number} {self.name}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
