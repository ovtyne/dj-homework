from django.db import models

NULLABLE = {'null': True, 'blank': True}


class BlogEntry(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')   # заголовок,
    slug = models.CharField(max_length=150, verbose_name='slug')     # slug(реализовать через CharField),
    body = models.TextField(verbose_name='содержимое', **NULLABLE)  # содержимое,
    preview = models.ImageField(verbose_name='превью', **NULLABLE)  # превью(изображение),
    creation_date = models.DateField(auto_now_add=True, verbose_name='дата создания')   # дата создания,
    is_published = models.BooleanField(default=False, verbose_name='опубликовано')     # признак публикации,
    view_counter = models.IntegerField(default=0, verbose_name='кол-во просмотров')    # количество просмотров.

    def __str__(self):
        return f'Название: {self.title} Создано: {self.creation_date} Просмотров:{self.view_counter}'

    class Meta:
        verbose_name = 'запись'
        verbose_name_plural = 'записи'
        ordering = ('title', 'creation_date', 'is_published', 'view_counter',)
