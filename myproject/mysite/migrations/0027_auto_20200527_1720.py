# Generated by Django 2.2 on 2020-05-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0026_auto_20200527_1531'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='product_count',
        ),
        migrations.AddField(
            model_name='deal',
            name='user_count_product',
            field=models.IntegerField(blank=True, default=1, verbose_name='Количество'),
        ),
    ]
