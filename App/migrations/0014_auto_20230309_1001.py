# Generated by Django 3.2.7 on 2023-03-09 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_order_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='cart',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
