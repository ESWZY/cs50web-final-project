from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name")
    sub = models.BooleanField(verbose_name="Is subscriber", default=0)

    def __str__(self):
        return f"{self.name}: {self.sub}"
