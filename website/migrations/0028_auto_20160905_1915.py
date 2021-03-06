# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-05 19:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0027_remove_post_release'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReleaseParent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('releases', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='release',
            field=models.ManyToManyField(blank=True, null=True, to='website.ReleaseParent'),
        ),
    ]
