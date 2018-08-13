# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-09 12:15
from __future__ import unicode_literals

from django.db import migrations


def add_service_to_pages(apps, schema_editor):
    Service = apps.get_model('core', 'Service')
    Page = apps.get_model('wagtailcore', 'Page')
    for page in Page.objects.all():
        if hasattr(page, 'view_app'):
            Service.objects.get_or_create(
                name=page.view_app,
                page=page
            )


def remove_service_from_page(apps, schema_editor):
    Service = apps.get_model('core', 'Service')
    Service.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180809_1215'),
    ]

    operations = [
        migrations.RunPython(
            add_service_to_pages,
            reverse_code=remove_service_from_page
        )
    ]
