# Generated by Django 3.0.3 on 2020-05-25 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0011_auto_20200525_0747'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='account_id',
            field=models.CharField(default=43697699, max_length=20),
        ),
    ]
