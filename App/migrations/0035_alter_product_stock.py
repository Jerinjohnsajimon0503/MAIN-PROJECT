# Generated by Django 4.2.1 on 2023-07-03 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0034_alter_product_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='stock',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
