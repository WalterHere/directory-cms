# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-12 09:55
from __future__ import unicode_literals

import wagtailmarkdown.fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('great_international', '0001_squashed_0015_auto_20190306_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalCuratedTopicLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('display_title', models.CharField(blank=True, null=True, max_length=255)),
                ('teaser', models.CharField(max_length=255)),
                ('feature_section_heading', models.CharField(max_length=255)),
                ('feature_one_heading', models.CharField(max_length=255)),
                ('feature_one_content', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('feature_two_heading', models.CharField(max_length=255)),
                ('feature_two_content', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('feature_one_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('feature_two_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('featured_page_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage')),
                ('featured_page_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage')),
                ('featured_page_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.InternationalArticlePage')),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('tags', modelcluster.fields.ParentalManyToManyField(blank=True, to='core.Tag')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
