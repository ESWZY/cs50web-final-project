from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from .models import Article


# Create your views here.
def index(request):
    return render(request, "articles/index.html")


def search(request):
    query = request.POST["query"]
    # https://docs.djangoproject.com/en/3.0/topics/db/queries/
    # Do not need try catch
    articles = Article.objects.filter(title__icontains=query)
    articles2 = Article.objects.filter(free_text__icontains=query)
    articles3 = Article.objects.filter(pay_text__icontains=query)
    articles = articles.union(articles2, articles3)
    context = {
        "articles": articles
    }
    return render(request, "articles/results.html", context)

