# Generated by Django 4.2.1 on 2023-06-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_alter_product_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='added_by',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
