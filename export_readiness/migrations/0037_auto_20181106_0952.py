# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-11-06 09:52
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('export_readiness', '0036_auto_20181105_1258'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactSuccessPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True)),
                ('heading', models.CharField(max_length=255, verbose_name='Title')),
                ('body_text', models.CharField(max_length=255, verbose_name='Body text')),
                ('next_title', models.CharField(max_length=255, verbose_name='Title')),
                ('next_body_text', models.CharField(max_length=255, verbose_name='Body text')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.RemoveField(
            model_name='deprecatedgetfinancepage',
            name='banner_image',
        ),
        migrations.RemoveField(
            model_name='deprecatedgetfinancepage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='deprecatedgetfinancepage',
            name='ukef_logo',
        ),
        migrations.DeleteModel(
            name='DeprecatedGetFinancePage',
        ),
    ]
