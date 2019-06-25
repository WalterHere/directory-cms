# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-29 10:39
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('invest', '0028_auto_20190503_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_image_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary',
            field=core.model_fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_ar',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_de',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_en_gb',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_es',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_fr',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_ja',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_pt',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_summary_zh_hans',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_one_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_image_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary',
            field=core.model_fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_ar',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_de',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_en_gb',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_es',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_fr',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_ja',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_pt',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_summary_zh_hans',
            field=core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_three_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_image_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_ar',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_de',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_en_gb',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_es',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_fr',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_ja',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_pt',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_summary_zh_hans',
            field=core.model_fields.MarkdownField(blank=True, max_length=255, null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investhomepage',
            name='featured_card_two_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='capital_invest_section_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_call_to_action_url_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_ar',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_de',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_en_gb',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_es',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_fr',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_ja',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_pt',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investhomepage',
            name='setup_guide_title_zh_hans',
            field=models.CharField(blank=True, default='Set up an overseas business in the UK', max_length=255, null=True),
        ),
    ]