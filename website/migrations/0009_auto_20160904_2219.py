# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-04 22:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20160904_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='releases',
        ),
        migrations.AddField(
            model_name='post',
            name='year_in_school',
            field=models.CharField(choices=[('FR', 'Freshman'), ('SO', 'Sophomore'), ('JR', 'Junior'), ('SR', 'Senior')], default='FR', max_length=2),
        ),
    ]