# Generated by Django 3.0.3 on 2020-06-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0035_auto_20200613_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderid',
            name='order_id',
            field=models.IntegerField(default=96768169),
        ),
    ]