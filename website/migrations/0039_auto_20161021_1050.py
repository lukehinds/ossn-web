# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0038_auto_20161017_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=select_multiple_field.models.SelectMultipleField(choices=[('icehouse', 'Icehouse'), ('juno', 'Juno'), ('kilo', 'Kilo'), ('liberty', 'Liberty'), ('mitaka', 'Mitaka'), ('newton', 'Newton')], default='newton', max_length=50),
        ),
    ]
