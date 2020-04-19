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
    # try:
    articles = Article.objects.filter(title__icontains=query)
    # except Article.DoesNotExist:
    #     raise Http404("Article does not exist")

    # ans = []
    # for article in articles:
    #     item = {
    #         'title': article.title,
    #         'free_text': article.free_text,
    #         'pat_text': article.pay_text
    #     }
    #     ans.append(item)
    context = {
        "articles": articles
    }
    return render(request, "articles/results.html", context)

