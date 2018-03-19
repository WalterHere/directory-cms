# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-16 16:07
from __future__ import unicode_literals

import core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
        ('find_a_supplier', '0015_auto_20180314_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryListPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('proposition_text', models.CharField(max_length=500)),
                ('proposition_text_en_gb', models.CharField(max_length=500, null=True)),
                ('proposition_text_de', models.CharField(max_length=500, null=True)),
                ('proposition_text_ja', models.CharField(max_length=500, null=True)),
                ('proposition_text_ru', models.CharField(max_length=500, null=True)),
                ('proposition_text_zh_hans', models.CharField(max_length=500, null=True)),
                ('proposition_text_fr', models.CharField(max_length=500, null=True)),
                ('proposition_text_es', models.CharField(max_length=500, null=True)),
                ('proposition_text_pt', models.CharField(max_length=500, null=True)),
                ('proposition_text_pt_br', models.CharField(max_length=500, null=True)),
                ('proposition_text_ar', models.CharField(max_length=500, null=True)),
                ('call_to_action_text', models.CharField(max_length=500)),
                ('call_to_action_text_en_gb', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_de', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_ja', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_ru', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_zh_hans', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_fr', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_es', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_pt', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_pt_br', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_ar', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=500)),
                ('breadcrumbs_label_en_gb', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_de', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_ja', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_ru', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_zh_hans', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_fr', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_es', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_pt', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_pt_br', models.CharField(max_length=500, null=True)),
                ('breadcrumbs_label_ar', models.CharField(max_length=500, null=True)),
                ('seo_description', models.CharField(max_length=1000)),
                ('seo_description_en_gb', models.CharField(max_length=1000, null=True)),
                ('seo_description_de', models.CharField(max_length=1000, null=True)),
                ('seo_description_ja', models.CharField(max_length=1000, null=True)),
                ('seo_description_ru', models.CharField(max_length=1000, null=True)),
                ('seo_description_zh_hans', models.CharField(max_length=1000, null=True)),
                ('seo_description_fr', models.CharField(max_length=1000, null=True)),
                ('seo_description_es', models.CharField(max_length=1000, null=True)),
                ('seo_description_pt', models.CharField(max_length=1000, null=True)),
                ('seo_description_pt_br', models.CharField(max_length=1000, null=True)),
                ('seo_description_ar', models.CharField(max_length=1000, null=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.AddTranslationsBrokerFieldsMixin, 'wagtailcore.page'),
        ),
    ]
