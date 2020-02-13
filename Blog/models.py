import uuid
from collections import defaultdict

from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField('Названеие статьи',  max_length=220)
    body = models.TextField('Текст статьи', default='')
    date = models.DateTimeField('Дата и время статьи', default=timezone.now())
    view = models.PositiveIntegerField('Просмотры', default=0)
    likes = models.PositiveIntegerField('Лайки', default=0)
    uuid = models.UUIDField('uuid', default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статью'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField('Автор', max_length=100)
    body = models.TextField('Текст комментария', default='')
    date = models.DateTimeField('Дата и время', default=timezone.now())

    def __str__(self):
        return self.author

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class Tag(models.Model):
    tag_id = models.ManyToManyField(Post)
    tag_name = models.CharField('Метка', max_length=50, unique=True)

    def __str__(self):
        return self.tag_name

    class Meta:
        verbose_name = 'Метку'
        verbose_name_plural = 'Метки'





