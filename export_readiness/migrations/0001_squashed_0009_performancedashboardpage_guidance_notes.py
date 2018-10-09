# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-09 13:41
from __future__ import unicode_literals

import core.fields
import core.models
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('export_readiness', '0001_initial'), ('export_readiness', '0002_auto_20180410_1038'), ('export_readiness', '0003_exportreadinessapp'), ('export_readiness', '0004_auto_20180423_1142'), ('export_readiness', '0005_auto_20180426_1521'), ('export_readiness', '0006_auto_20180427_1518'), ('export_readiness', '0007_getfinancepage'), ('export_readiness', '0008_performancedashboardpage'), ('export_readiness', '0009_performancedashboardpage_guidance_notes')]

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
    ]

    operations = [
        migrations.CreateModel(
            name='TermsAndConditionsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='ExportReadinessApp',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='PrivacyAndCookiesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='GetFinancePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('banner_content', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('section_one_content', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('section_two_content', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('video_embed', models.CharField(max_length=500)),
                ('section_three_content', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('call_to_action_text', models.CharField(max_length=255)),
                ('call_to_action_url', models.CharField(max_length=500)),
                ('banner_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('ukef_logo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.CreateModel(
            name='PerformanceDashboardPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(max_length=255)),
                ('description', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('product_link', models.URLField()),
                ('data_title_row_one', models.CharField(max_length=100)),
                ('data_number_row_one', models.CharField(max_length=15)),
                ('data_period_row_one', models.CharField(max_length=100)),
                ('data_description_row_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('data_title_row_two', models.CharField(max_length=100)),
                ('data_number_row_two', models.CharField(max_length=15)),
                ('data_period_row_two', models.CharField(max_length=100)),
                ('data_description_row_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('data_title_row_three', models.CharField(max_length=100)),
                ('data_number_row_three', models.CharField(max_length=15)),
                ('data_period_row_three', models.CharField(max_length=100)),
                ('data_description_row_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('data_title_row_four', models.CharField(blank=True, max_length=100, null=True)),
                ('data_number_row_four', models.CharField(blank=True, max_length=15, null=True)),
                ('data_period_row_four', models.CharField(blank=True, max_length=100, null=True)),
                ('data_description_row_four', core.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('landing_dashboard', models.BooleanField(default=False)),
                ('guidance_notes', core.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
