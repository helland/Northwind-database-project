# Generated by Django 5.1.6 on 2025-03-11 14:47

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductList',
            fields=[
                ('product_list_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'product_lists',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ProductListEntry',
            fields=[
                ('entry_id', models.AutoField(primary_key=True, serialize=False)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
                ('product_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='main.productlist')),
            ],
            options={
                'db_table': 'product_list_entries',
                'managed': True,
            },
        ),
    ]
