# Generated by Django 3.0.3 on 2020-04-20 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20200420_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='brief',
            field=models.TextField(null=True, verbose_name='Brief'),
        ),
    ]
