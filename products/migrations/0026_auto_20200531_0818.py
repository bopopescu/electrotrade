# Generated by Django 3.0.3 on 2020-05-31 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_auto_20200529_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orderid',
            name='order_id',
            field=models.IntegerField(default=71714611),
        ),
    ]