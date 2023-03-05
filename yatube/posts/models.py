from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200)
    title.verbose_name = 'Название группы'
    slug = models.SlugField(max_length=200, unique=True)
    slug.verbose_name = 'URL часть адреса группы'
    description = models.TextField(max_length=500)
    description.verbose_name = 'Описание группы'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Создание группы для постов'


class Post(models.Model):
    text = models.TextField()
    text.verbose_name = 'Текст поста'
    pub_date = models.DateTimeField(auto_now_add=True)
    pub_date.verbose_name = 'Дата публикации поста'
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    author.verbose_name = 'Автор поста'
    group = models.ForeignKey(
        to=Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts_set'
    )
    group.verbose_name = 'Группа к которой относится пост'

    class Meta:
        verbose_name = 'Создание самих постов'
        ordering = ('-pub_date',)
