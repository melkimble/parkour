# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-07 15:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0017_sample_is_pooled'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='index_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.IndexType', verbose_name='Index Type'),
        ),
        migrations.AlterField(
            model_name='library',
            name='index_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.IndexType', verbose_name='Index Type'),
        ),
    ]
