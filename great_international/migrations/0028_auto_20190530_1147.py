# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-30 11:47
from __future__ import unicode_literals

import wagtailmarkdown.fields
import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0027_auto_20190529_1033'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='buy_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='invest_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_intro_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestopportunitypage',
            name='next_steps_title_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='buy_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='invest_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_intro_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionalsectorpage',
            name='next_steps_title_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='buy_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='invest_cta_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_intro_zh_hans',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_ar',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_de',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_en_gb',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_es',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_fr',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_ja',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_pt',
        ),
        migrations.RemoveField(
            model_name='capitalinvestregionpage',
            name='next_steps_title_zh_hans',
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_text_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestopportunitypage',
            name='contact_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_text_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionalsectorpage',
            name='contact_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_text_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='capitalinvestregionpage',
            name='contact_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
