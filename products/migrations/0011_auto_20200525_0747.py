# Generated by Django 3.0.3 on 2020-05-25 07:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200524_1234'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addcart',
            old_name='cgst_value',
            new_name='gst_value',
        ),
        migrations.RenameField(
            model_name='addcart',
            old_name='igst_value',
            new_name='per_product_price',
        ),
        migrations.RenameField(
            model_name='orderproduct',
            old_name='cgst_per',
            new_name='gst_per',
        ),
        migrations.RenameField(
            model_name='products',
            old_name='cgst_per',
            new_name='gst_per',
        ),
        migrations.RemoveField(
            model_name='addcart',
            name='sgst_value',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='cgst_value',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='igst_per',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='igst_value',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='sgst_per',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='sgst_value',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='total',
        ),
        migrations.RemoveField(
            model_name='products',
            name='igst_per',
        ),
        migrations.RemoveField(
            model_name='products',
            name='replacement_from',
        ),
        migrations.RemoveField(
            model_name='products',
            name='replacement_to',
        ),
        migrations.RemoveField(
            model_name='products',
            name='sgst_per',
        ),
        migrations.AddField(
            model_name='addcart',
            name='delivery_charges',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='delivery_charges',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='delivery_days',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='delivery_status',
            field=models.CharField(default='Your Order Has Placed', max_length=200),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='is_replacement',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='replacement_from',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='replacement_to',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='delivery_charges',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='products',
            name='replacement_duration',
            field=models.IntegerField(choices=[('1 Month', 1), ('2 Months', 2), ('3 Months', 3), ('4 Months', 4), ('5 Months', 5), ('6 Months', 6), ('7 Months', 7), ('8 Months', 8), ('9 Months', 9), ('10 Months', 10), ('11 Months', 11), ('12 Months', 12), ('2 Years', 24), ('3 Years', 36)], default=0),
        ),
        migrations.AlterField(
            model_name='banner',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='orderid',
            name='order_id',
            field=models.IntegerField(default=39707392),
        ),
        migrations.CreateModel(
            name='ProductIGST',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('igst_value', models.FloatField(default=None)),
                ('igst_per', models.FloatField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.Products', unique=True)),
            ],
        ),
    ]