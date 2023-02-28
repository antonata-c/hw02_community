from django.shortcuts import render, get_object_or_404
from .models import Post, Group
# Create your views here.


def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    title = 'Последние обновления на сайте'
    posts = Post.objects.order_by('-pub_date')[:10]
    # В словаре context отправляем информацию в шаблон
    context = {
        'title': title,
        'text': text,
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    text = 'Лев Толстой – зеркало русской революции.'
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    context = {
        'text': text,
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
