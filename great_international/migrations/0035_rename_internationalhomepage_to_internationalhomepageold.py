# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailcore', '0040_page_draft_title'),
        ('great_international', '0034_populate_apppage_fields_from_homepage'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InternationalHomePage',
            new_name='InternationalHomePageOld',
        ),
    ]
