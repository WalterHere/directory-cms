# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-29 09:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtaildocs', '0008_document_file_size'),
        ('great_international', '0011_internationalcapitalinvestlandingpage_energy_sector_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalcapitalinvestlandingpage',
            name='pdf_document',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document'),
        ),
    ]
