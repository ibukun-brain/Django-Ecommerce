# Generated by Django 3.2.7 on 2023-02-24 13:01

import auto_prefetch
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0007_auto_20230215_1029'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visible', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('review_title', models.CharField(max_length=100)),
                ('comment', models.TextField(blank=True, max_length=250)),
                ('stars', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0.5)])),
                ('reviewed', models.BooleanField(default=False)),
                ('order', auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.order')),
                ('product', auto_prefetch.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('user', auto_prefetch.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'prefetch_manager',
            },
            managers=[
                ('objects', django.db.models.manager.Manager()),
                ('prefetch_manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
