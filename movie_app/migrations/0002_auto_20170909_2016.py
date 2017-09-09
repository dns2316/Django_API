# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-09 20:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='movie',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(max_length=1500),
        ),
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.URLField(max_length=225),
        ),
        migrations.AlterField(
            model_name='movie',
            name='url',
            field=models.URLField(max_length=41),
        ),
    ]