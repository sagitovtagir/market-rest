# Generated by Django 2.2 on 2020-05-27 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0021_deal'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(blank=True, default=0, verbose_name='Цена'),
        ),
    ]
