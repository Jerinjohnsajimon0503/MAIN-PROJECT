# Generated by Django 3.2.7 on 2023-03-05 09:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_order_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='is_delivery_man',
            new_name='is_shopkeeper',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deliveryManAddress',
            new_name='shopkeeperAddress',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deliveryManName',
            new_name='shopkeeperLocation',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='manufacturerAddress',
            new_name='shopkeeperName',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='deliveryManPhone',
            new_name='shopkeeperPhone',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='is_manufacturer',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='manufacturerLocation',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='manufacturerName',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='manufacturerPhone',
        ),
    ]
