# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-03 21:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='recommendedactions',
            new_name='actions',
        ),
    ]
