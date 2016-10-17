# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import select_multiple_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0036_post_releases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='releases',
            field=select_multiple_field.models.SelectMultipleField(choices=[('juno', 'Juno'), ('kilo', 'Kilo'), ('liberty', 'Liberty')], max_length=10, default='liberty'),
        ),
    ]
