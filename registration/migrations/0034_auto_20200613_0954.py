# Generated by Django 3.0.3 on 2020-06-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0033_auto_20200602_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='account_id',
            field=models.CharField(default=58979230, max_length=20),
        ),
    ]
