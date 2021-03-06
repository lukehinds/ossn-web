# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-03 21:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ossn', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=200)),
                ('releases', models.CharField(max_length=200)),
                ('discussion', models.TextField()),
                ('summary', models.TextField()),
                ('recommendedactions', models.TextField()),
                ('contact', models.CharField(max_length=50)),
                ('references', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
