from django.db import models
from django_random_queryset import RandomManager

# Create your models here.
class Article(models.Model):
    objects = RandomManager()
    title = models.TextField(verbose_name='Title')
    author = models.CharField(max_length=64, verbose_name='Author', null=True)
    date = models.CharField(max_length=64, verbose_name='Publish date', null=True)
    brief = models.TextField(verbose_name='Brief', null=True)
    free_text = models.TextField(verbose_name='Free part', null=True)
    pay_text = models.TextField(verbose_name='Full part', null=True)
