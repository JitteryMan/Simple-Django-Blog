import uuid
from django.db import models


class Post(models.Model):
    title = models.CharField('title_post',  max_length=220)
    body = models.TextField('text_post')
    date = models.DateTimeField('date_time_post')
    view = models.PositiveIntegerField('views_post')
    likes = models.PositiveIntegerField('likes_post')
    uuid = models.UUIDField('uuid', default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f'{self.title} [{self.uuid}]'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class Comment(models.Model):
    post_id = models.ForeignKey(Post, unique=True, on_delete=models.CASCADE)
    author = models.CharField('author_field', max_length=100)
    date = models.DateTimeField('date_time_field')



class Tag(models.Model):
    pass



