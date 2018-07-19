# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-19 13:02
from __future__ import unicode_literals

from django.db import migrations


def migrate_sector_pages_info_streamfields(apps, schema_editor):

    SectorPage = apps.get_model('invest', 'SectorPage')
    for page in SectorPage.objects.all():

        for index, subsection in enumerate(page.subsections, 1):
            if 'info' in subsection.value:
                field_name = 'subsection_content_{}_en_gb'.format(
                    NUMBER_MAPPING[index]
                )
                setattr(page, field_name, subsection.value['info'])
        page.save()


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0005_auto_20180719_1301'),
    ]

    operations = [
        migrations.RunPython(
            migrate_sector_pages_info_streamfields,
            reverse_code=migrations.RunPython.noop
        ),
    ]