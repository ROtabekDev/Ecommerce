# Generated by Django 4.2 on 2023-04-17 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='discout_price',
            new_name='discount_price',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='user',
        ),
    ]
