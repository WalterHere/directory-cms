# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-04 13:20
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('great_international', '0008_auto_20190404_1320'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_ar',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_de',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_en_gb',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_es',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_fr',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_ja',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_pt',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_pt_br',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_ru',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_body_text_zh_hans',
            field=core.model_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_pt_br',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_image_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_ar',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_de',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_en_gb',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_es',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_fr',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_ja',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_pt',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_pt_br',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_ru',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_subheading_zh_hans',
            field=models.CharField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_teaser_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_ar',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_de',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_en_gb',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_es',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_fr',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_ja',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_pt',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_pt_br',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_ru',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='article_title_zh_hans',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_pt_br',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_one_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_pt_br',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_three_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_pt_br',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_ru',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
        migrations.AddField(
            model_name='internationalarticlepage',
            name='related_page_two_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage'),
        ),
    ]
