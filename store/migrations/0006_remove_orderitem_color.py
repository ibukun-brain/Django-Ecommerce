# Generated by Django 3.2.7 on 2023-01-30 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_remove_product_available_colors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='color',
        ),
    ]
