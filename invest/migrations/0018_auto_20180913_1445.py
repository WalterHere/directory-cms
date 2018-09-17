# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-13 14:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('invest', '0017_auto_20180911_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighPotentialOpportunityFormSuccessPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=255, verbose_name='section title')),
                ('sub_heading', models.CharField(max_length=255, verbose_name='section body')),
                ('next_steps_title', models.CharField(max_length=255, verbose_name='section title')),
                ('next_steps_body', models.CharField(max_length=255, verbose_name='section body')),
                ('documents_title', models.CharField(max_length=255, verbose_name='section title')),
                ('documents_body', models.CharField(max_length=255, verbose_name='section body')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AddField(
            model_name='highpotentialopportunitydetailpage',
            name='pdf_document_url',
            field=models.URLField(default='', help_text='The link to the PDF document.'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='highpotentialopportunitydetailpage',
            name='summary_image',
            field=models.ForeignKey(blank=True, help_text='Image used on opportunity listing page for this opportunity', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='case_study_one_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='opportunity_list_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]