# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mistake',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('text', models.CharField(max_length=500)),
                ('tag', models.CharField(max_length=100)),
                ('correction', models.CharField(max_length=500)),
                ('start_idx', models.IntegerField()),
                ('weight_language', models.CharField(null=True, choices=[('Minor', 'Minor'), ('Major', 'Major'), ('Critical', 'Critical')], max_length=10, blank=True)),
                ('weight_understanding', models.CharField(null=True, choices=[('Minor', 'Minor'), ('Major', 'Major'), ('Critical', 'Critical')], max_length=10, blank=True)),
                ('delete', models.NullBooleanField()),
                ('cause', models.CharField(null=True, choices=[('Typo', 'Typo'), ('L1_interference', 'L1 interference'), ('Absence_of_Category_in_L1', 'Absence of Category in L1'), ('Other', 'Other')], max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('sentence', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('path', models.TextField()),
                ('department', models.CharField(max_length=500)),
                ('type', models.CharField(choices=[('graph_description', 'graph description'), ('opinion_essay', 'opinion essay')], max_length=20)),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('pos', models.CharField(max_length=10)),
                ('lemma', models.CharField(max_length=100)),
                ('wordform', models.CharField(max_length=100)),
                ('start_idx', models.IntegerField()),
                ('mistake', models.ManyToManyField(null=True, to='search_app.Mistake', blank=True)),
                ('sentence', models.ForeignKey(to='search_app.Sentence')),
            ],
        ),
        migrations.AddField(
            model_name='sentence',
            name='text',
            field=models.ForeignKey(to='search_app.Text'),
        ),
        migrations.AddField(
            model_name='mistake',
            name='sentence',
            field=models.ForeignKey(to='search_app.Sentence'),
        ),
    ]
