# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-04 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20160904_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=models.CharField(choices=[('JO', 'Juno'), ('KO', 'Kilo'), ('LY', 'Liberty'), ('MA', 'Mitaka')], default='MA', max_length=2),
        ),
    ]
