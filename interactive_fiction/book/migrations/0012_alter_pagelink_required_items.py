# Generated by Django 4.2.1 on 2023-05-30 14:03
from __future__ import annotations

from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0011_pagelink_required_items_alter_bookpage_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagelink',
            name='required_items',
            field=models.ManyToManyField(blank=True, db_column='items', to='book.item'),
        ),
    ]
