# Generated by Django 2.2.6 on 2020-04-15 16:08

from decimal import Decimal
from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('quantity', models.PositiveIntegerField()),
                ('rating', models.PositiveSmallIntegerField(default=0)),
                ('description', models.TextField(default='Product description.')),
                ('image_url', models.TextField(default='')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'products',
            },
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('products', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), default=[], size=None)),
                ('quantities', django.contrib.postgres.fields.ArrayField(base_field=models.PositiveIntegerField(), default=[], size=None)),
                ('total_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('delivery_method', models.CharField(default='', max_length=30)),
                ('payment_method', models.CharField(default='', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
    ]
