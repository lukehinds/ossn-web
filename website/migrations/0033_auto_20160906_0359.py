# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-06 03:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0032_auto_20160906_0354'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='releases',
        ),
        migrations.DeleteModel(
            name='Release',
        ),
    ]
