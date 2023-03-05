from django.shortcuts import render, get_object_or_404
from .models import Post, Group

COUNT_POSTS: int = 10


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    title = 'Последние обновления на сайте'
    posts = Post.objects.all()[:COUNT_POSTS]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    text = 'Лев Толстой – зеркало русской революции.'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_set.all()[:COUNT_POSTS]
    context = {
        'text': text,
        'groupч': group,
        'posts': posts,
    }

    return render(request, template, context)
