# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 11:58
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    call_command('loaddata', 'concentration_methods_sequencing_run_conditions', app_label='library')


def unload_fixture(apps, schema_editor):
    ConcentrationMethod = apps.get_model('library', 'ConcentrationMethod')
    SequencingRunCondition = apps.get_model('library', 'SequencingRunCondition')
    SequencingRunCondition.objects.all().delete()
    ConcentrationMethod.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_concentrationmethod_sequencingruncondition'),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture)
    ]
