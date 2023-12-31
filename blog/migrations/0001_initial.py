# Generated by Django 4.2.5 on 2023-09-13 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(blank=True, null=True, verbose_name='содержимое')),
                ('preview', models.ImageField(blank=True, null=True, upload_to='', verbose_name='превью')),
                ('creation_date', models.DateField(auto_now_add=True, verbose_name='дата создания')),
                ('is_published', models.BooleanField(default=False, verbose_name='опубликовано')),
                ('view_counter', models.IntegerField(default=0, verbose_name='кол-во просмотров')),
            ],
            options={
                'verbose_name': 'запись',
                'verbose_name_plural': 'записи',
                'ordering': ('title', 'creation_date', 'is_published', 'view_counter'),
            },
        ),
    ]
