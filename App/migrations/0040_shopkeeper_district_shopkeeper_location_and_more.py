# Generated by Django 4.2.1 on 2023-07-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0039_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopkeeper',
            name='district',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='location',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='pin',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shopkeeper',
            name='street',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]