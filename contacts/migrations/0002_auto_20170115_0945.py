# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-15 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=254),
        ),
    ]
