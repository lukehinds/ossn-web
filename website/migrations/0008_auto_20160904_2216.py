# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-04 22:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20160904_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=models.CharField(choices=[(1, 'Juno'), (2, 'Kilo'), (3, 'Liberty'), (4, 'Mitaka')], default=1, max_length=2),
        ),
    ]
