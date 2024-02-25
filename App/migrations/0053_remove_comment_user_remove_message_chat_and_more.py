# Generated by Django 4.2.3 on 2024-02-24 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0052_product_selladdress_product_sellphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='message',
            name='chat',
        ),
        migrations.RenameField(
            model_name='rating',
            old_name='doctor',
            new_name='product',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]