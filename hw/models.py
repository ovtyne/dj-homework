from django.db import models

NULLABLE = {'null': True, 'blank': True}


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='наименование')                              # наименование,
    description = models.TextField(verbose_name='описание')                                            # описание,
    image = models.ImageField(**NULLABLE)                                                              # изображение,
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='категория')    # категория,
    price = models.FloatField(verbose_name='цена')                          # цена за покупку,
    creation_date = models.DateField(verbose_name='дата создания', auto_now_add=True)          # дата создания,
    change_date = models.DateField(verbose_name='дата изменения', auto_now=True)           # дата последнего изменения.

    def __str__(self):
        return f'{self.title} {self.category} {self.price}'

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
