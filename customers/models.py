from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=64, verbose_name="Name", default='SOME STRING')
    sub = models.BooleanField(verbose_name="Is subscriber", default=0)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    credit_card = models.CharField(max_length=19, verbose_name="Credit card", null=True)
    card_balance = models.IntegerField(verbose_name="Balance", null=True)

    def __str__(self):
        return f"{self.name}: {self.sub}"
