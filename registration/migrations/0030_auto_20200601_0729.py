# Generated by Django 3.0.3 on 2020-06-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0029_auto_20200601_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='account_id',
            field=models.CharField(default=34014111, max_length=20),
        ),
    ]