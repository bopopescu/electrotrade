# Generated by Django 3.0.3 on 2020-05-19 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20200519_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='is_replacement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='products',
            name='replacement_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='replacement_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderid',
            name='order_id',
            field=models.IntegerField(default=49916008),
        ),
    ]