# Generated by Django 4.2.1 on 2023-07-02 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0029_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
