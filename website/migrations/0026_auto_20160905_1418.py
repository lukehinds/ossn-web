# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-05 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0025_auto_20160905_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release',
            field=models.CharField(choices=[('j', 'Juno'), ('k', 'Kilo'), ('l', 'Liberty')], max_length=10),
        ),
    ]
