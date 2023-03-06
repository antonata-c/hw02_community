from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=200, verbose_name='group title')
    slug = models.SlugField(max_length=100,
                            unique=True,
                            verbose_name='group slug')
    description = models.TextField(verbose_name='group description')

    def __str__(self):
        return self.title


class Post(models.Model):
    text = models.TextField(verbose_name='post text')
    pub_date = models.DateTimeField(auto_now_add=True,
                                    verbose_name='post date')
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts',
        verbose_name='post group',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='post author'
    )

    def __str__(self):
        return self.text[:settings.POST_TEXT_LENGTH]

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-pub_date']
