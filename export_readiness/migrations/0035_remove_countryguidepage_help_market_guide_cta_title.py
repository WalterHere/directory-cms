# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-14 16:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0034_auto_20190314_1250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='countryguidepage',
            name='help_market_guide_cta_title',
        ),
    ]
