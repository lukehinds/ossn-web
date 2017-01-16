# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0039_auto_20161021_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=select_multiple_field.models.SelectMultipleField(default='ocata', max_length=50, choices=[('icehouse', 'Icehouse'), ('juno', 'Juno'), ('kilo', 'Kilo'), ('liberty', 'Liberty'), ('mitaka', 'Mitaka'), ('ocata', 'Ocata')]),
        ),
    ]
