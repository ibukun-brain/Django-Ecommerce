# Generated by Django 3.2.7 on 2023-01-20 11:29

import auto_prefetch
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20230120_1229'),
        ('store', '0002_auto_20230114_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_address',
            field=auto_prefetch.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.address'),
        ),
    ]