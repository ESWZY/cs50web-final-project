from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.TextField(verbose_name='Title')
    author = models.CharField(max_length=64, verbose_name='Author', null=True)
    brief = models.TextField(verbose_name='Brief', null=True)
    free_text = models.TextField(verbose_name='Free part', null=True)
    pay_text = models.TextField(verbose_name='Full part', null=True)
