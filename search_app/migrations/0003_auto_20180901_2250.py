# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0002_auto_20180901_2248'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='word_mistake',
            new_name='mistake',
        ),
    ]
