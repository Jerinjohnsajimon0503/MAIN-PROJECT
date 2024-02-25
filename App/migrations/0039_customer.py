# Generated by Django 4.2.1 on 2023-07-11 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0038_alter_cart_quantity_alter_order_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=500)),
                ('email', models.CharField(blank=True, max_length=500)),
                ('phone', models.CharField(blank=True, max_length=500)),
                ('address', models.CharField(blank=True, max_length=5000)),
                ('balance', models.IntegerField(default=30000)),
            ],
        ),
    ]
