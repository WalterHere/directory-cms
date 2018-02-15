# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-14 20:55
from __future__ import unicode_literals

from django.db import migrations, models
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='casestudypage',
            name='body_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='body_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='companies_section_title_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_text_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='footer_title_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='key_facts_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='lede_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='casestudypage',
            name='read_more_text_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='description_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='image_alt_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='name_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_ar',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_de',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_en_gb',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_es',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_fr',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_ja',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_pt',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_pt_br',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='url_zh_hans',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='company_name_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_alt_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='image_caption_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='synopsis_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_ar',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_company_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_de',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_en_gb',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_es',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_fr',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_ja',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_name_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_pt',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_pt_br',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='testimonial_zh_hans',
            field=wagtail.wagtailcore.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='showcase',
            name='title_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
