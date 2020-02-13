# Generated by Django 3.0.3 on 2020-02-13 17:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Статью', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Метку', 'verbose_name_plural': 'Метки'},
        ),
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='', verbose_name='Текст комментария'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 13, 17, 51, 57, 13021, tzinfo=utc), verbose_name='Дата и время'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default='', verbose_name='Текст статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 13, 17, 51, 56, 927023, tzinfo=utc), verbose_name='Дата и время статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.PositiveIntegerField(default=0, verbose_name='Лайки'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=220, verbose_name='Названеие статьи'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view',
            field=models.PositiveIntegerField(default=0, verbose_name='Просмотры'),
        ),
        migrations.RemoveField(
            model_name='tag',
            name='tag_id',
        ),
        migrations.AddField(
            model_name='tag',
            name='tag_id',
            field=models.ManyToManyField(to='Blog.Post'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='tag_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Метка'),
        ),
    ]
