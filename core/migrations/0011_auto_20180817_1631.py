# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-17 16:18
from __future__ import unicode_literals

from django.db import migrations

from core.models import BasePage


def populate_service_name(apps, schema_editor):
    for sub_class in BasePage.__subclasses__():
        historic_model = apps.get_model(
            sub_class._meta.app_label, sub_class._meta.object_name
        )

        for page in historic_model.objects.all():
            page.service_name = sub_class.service_name_value
            page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20180815_1304'),
    ]

    operations = [
        migrations.RunPython(
            populate_service_name, reverse_code=migrations.RunPython.noop
        )
    ]
