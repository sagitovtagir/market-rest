# Generated by Django 2.2 on 2020-05-16 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20200516_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(default=16, on_delete=django.db.models.deletion.SET_DEFAULT, to='mysite.Category', verbose_name='Категория'),
        ),
    ]
