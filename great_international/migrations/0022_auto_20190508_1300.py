# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-08 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0021_auto_20190423_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page'),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_ar',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_de',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_en_gb',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_es',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_fr',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_ja',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_pt',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_subheading_zh_hans',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page'),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ar',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_de',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_en_gb',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_es',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_fr',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ja',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_pt',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_zh_hans',
            field=models.TextField(help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_ar',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_de',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_en_gb',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_es',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_fr',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_ja',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_pt',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_title_zh_hans',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_en_gb',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='internationalsectorpage',
            name='sub_heading_zh_hans',
            field=models.TextField(blank=True, null=True),
        ),
    ]
