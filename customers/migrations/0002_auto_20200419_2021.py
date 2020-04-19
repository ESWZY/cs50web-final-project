# Generated by Django 3.0.3 on 2020-04-19 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='address',
        ),
        migrations.AddField(
            model_name='customer',
            name='sub',
            field=models.BooleanField(default=0, verbose_name='Is subscriber'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
    ]
