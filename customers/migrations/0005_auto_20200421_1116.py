# Generated by Django 3.0.3 on 2020-04-21 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_auto_20200421_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='card_balance',
            field=models.IntegerField(verbose_name='Balance'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='credit_card',
            field=models.CharField(max_length=19, verbose_name='Credit card'),
        ),
    ]
