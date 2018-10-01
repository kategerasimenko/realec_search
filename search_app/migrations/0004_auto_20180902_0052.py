# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_app', '0003_auto_20180901_2250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mistake',
            name='delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='word',
            name='mistake',
            field=models.ManyToManyField(to='search_app.Mistake'),
        ),
    ]
