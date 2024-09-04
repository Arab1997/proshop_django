# Generated by Django 5.1 on 2024-09-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='shippingaddress',
            name='shippingPrice',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
