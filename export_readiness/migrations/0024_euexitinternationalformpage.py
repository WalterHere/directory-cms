# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 15:34
from __future__ import unicode_literals

import core.fields
import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('export_readiness', '0023_auto_20181001_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='EUExitInternationalFormPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('first_name_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('first_name_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('last_name_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('last_name_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('email_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('email_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('organisation_type_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('organisation_type_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('company_name_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('company_name_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('country_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('country_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('city_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('city_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
                ('comment_label', core.fields.FormLabelField(max_length=200, verbose_name='label')),
                ('comment_help_text', core.fields.FormHelpTextField(blank=True, max_length=200, null=True, verbose_name='Help text')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
    ]
