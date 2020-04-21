from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.db.models import Q
from .models import Article


# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def search(request):
    query = request.POST["query"]
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/
    # Do not need try catch
    # https://docs.djangoproject.com/en/dev/topics/db/queries/#complex-lookups-with-q-objects
    # Use Q and , | to replace AND OR
    articles = Article.objects.filter(Q(title__icontains=query) |
                                      Q(free_text__icontains=query) |
                                      Q(pay_text__icontains=query)).order_by('-id')  # Notice the - before 'id'
    context = {
        "articles": articles,
        "query": query,
    }
    return render(request, "articles/results.html", context)


def article(request, title):
    title = title.replace('-', ' ')
    article = Article.objects.get(title=title)
    context = {
        "article": article
    }
    return render(request, "articles/article.html", context)


def discovery(request):
    articles = Article.objects.filter()
    # https://github.com/rremizov/django-random-queryset
    articles = articles.random(10)
    context = {
        "articles": articles.order_by('-id'),
        "query": '',
    }
    return render(request, "articles/results.html", context)
