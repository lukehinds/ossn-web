# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0035_auto_20160906_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='releases',
            field=select_multiple_field.models.SelectMultipleField(max_length=10, choices=[('a', 'Juno'), ('b', 'Kilo'), ('p', 'Liberty')], default='a'),
        ),
    ]
