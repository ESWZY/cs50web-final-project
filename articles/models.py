from django.db import models


# Create your models here.
class Article(models.Model):
    title = models.TextField(verbose_name='Title')
    free_text = models.TextField(verbose_name='Free part')
    pay_text = models.TextField(verbose_name='Full part')
