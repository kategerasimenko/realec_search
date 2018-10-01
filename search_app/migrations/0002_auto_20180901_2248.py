# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='mistake',
            new_name='word_mistake',
        ),
    ]
