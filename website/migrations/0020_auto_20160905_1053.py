# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-05 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_auto_20160905_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='release',
            field=models.IntegerField(choices=[(1, 'Juno'), (2, 'Kilo'), (3, 'Liberty')]),
        ),
    ]
