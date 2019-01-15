# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-15 10:58
from __future__ import unicode_literals

import core.model_fields
import core.models
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('export_readiness', '0044_auto_20181214_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='SitePolicyPages',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components')], db_index=True, max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='contactusguidancepage',
            name='topic',
            field=models.TextField(choices=[('alerts-not-relevant', 'Guidance - Daily alerts are not relevant'), ('opportunity-no-response', 'Guidance - Export Opportunity application no response'), ('no-verification-email', 'Guidance - Email verification missing'), ('password-reset', 'Guidance - Missing password reset link'), ('companies-house-login', 'Guidance - Companies House login not working'), ('verification-letter-code', 'Guidance - Where to enter letter verification code'), ('no-verification-letter', 'Guidance - Verification letter not delivered'), ('company-not-found', 'Guidance - Company not found')], help_text='The slug and CMS page title are inferred from the topic', unique=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardnotespage',
            name='body',
            field=core.model_fields.MarkdownField(help_text='Please include an h1 in this field e.g. # Heading level 1', validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='product_link',
            field=models.TextField(choices=[('https://www.great.gov.uk', 'Great.gov.uk'), ('https://selling-online-overseas.export.great.gov.uk', 'Selling Online Overseas'), ('https://www.great.gov.uk/export-opportunities/', 'Export Opportunities'), ('https://www.great.gov.uk/find-a-buyer/', 'Business Profiles'), ('https://invest.great.gov.uk', 'Invest in Great Britain')], help_text='The slug and page heading are inferred from the product link', unique=True),
        ),
    ]
