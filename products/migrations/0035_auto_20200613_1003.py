# Generated by Django 3.0.3 on 2020-06-13 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0034_auto_20200613_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderaddress',
            name='pincode',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='orderid',
            name='order_id',
            field=models.IntegerField(default=50729172),
        ),
    ]
