# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 11:46
from __future__ import unicode_literals

import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
        ('export_readiness', '0047_allcontactpagespage'),
        ('great_international', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalCampaignPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('campaign_heading', models.CharField(max_length=255)),
                ('section_one_heading', models.CharField(max_length=255)),
                ('section_one_intro', core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('selling_point_one_heading', models.CharField(max_length=255)),
                ('selling_point_one_content', core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('selling_point_two_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('selling_point_two_content', core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('selling_point_three_heading', models.CharField(blank=True, max_length=255, null=True)),
                ('selling_point_three_content', core.model_fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('section_one_contact_button_url', models.CharField(blank=True, max_length=255, null=True)),
                ('section_one_contact_button_text', models.CharField(blank=True, max_length=255, null=True)),
                ('section_two_heading', models.CharField(max_length=255)),
                ('section_two_intro', core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('section_two_contact_button_url', models.CharField(blank=True, max_length=255, null=True)),
                ('section_two_contact_button_text', models.CharField(blank=True, max_length=255, null=True)),
                ('related_content_heading', models.CharField(max_length=255)),
                ('related_content_intro', core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('cta_box_message', models.CharField(max_length=255)),
                ('cta_box_button_url', models.CharField(max_length=255)),
                ('cta_box_button_text', models.CharField(max_length=255)),
                ('campaign_hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('related_page_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage')),
                ('related_page_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage')),
                ('related_page_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage')),
                ('section_one_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('section_two_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('selling_point_one_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('selling_point_three_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('selling_point_two_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='greatinternationalapp',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internationalhomepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internationalmarketingpages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
    ]
