# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0037_auto_20161017_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=select_multiple_field.models.SelectMultipleField(max_length=50, choices=[('juno', 'Juno'), ('kilo', 'Kilo'), ('liberty', 'Liberty')], default='liberty'),
        ),
    ]
