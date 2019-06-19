# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-22 14:56
from __future__ import unicode_literals

from directory_constants import cms
from django.db import migrations


def add_service_name_to_existing_apps(apps, schema_editor):
    InvestApp = apps.get_model('invest', 'InvestApp')
    FASApp = apps.get_model('find_a_supplier', 'FindASupplierApp')
    ExReadApp = apps.get_model('export_readiness', 'ExportReadinessApp')
    InvestApp.objects.all().update(service_name=cms.INVEST)
    FASApp.objects.all().update(service_name=cms.FIND_A_SUPPLIER)
    ExReadApp.objects.all().update(service_name=cms.EXPORT_READINESS)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20180822_0915'),
        ('export_readiness', '0013_exportreadinessapp_service_name'),
        ('find_a_supplier', '0062_auto_20180817_1630_squashed_0065_auto_20180829_1027'),
        ('invest', '0009_investapp_service_name')
    ]

    operations = [
        migrations.RunPython(
            add_service_name_to_existing_apps,
            reverse_code=migrations.RunPython.noop,
            elidable=True
        )
    ]
