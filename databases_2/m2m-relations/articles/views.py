from django.views.generic import ListView
from django.shortcuts import render

from .models import Article, Tag, ArticleTag


def articles_list(request):
    template = 'articles/news.html'
    objects_list = Article.objects.all()
    context = {'object_list': objects_list}
    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    ordering = '-published_at'

    return render(request, template, context=context)
