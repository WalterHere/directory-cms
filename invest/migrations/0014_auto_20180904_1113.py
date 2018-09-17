# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-04 11:13
from __future__ import unicode_literals

import core.fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('wagtailimages', '0021_image_file_hash'),
        ('wagtailcore', '0040_page_draft_title'),
        ('invest', '0013_auto_20180830_0632'),
    ]

    operations = [
        migrations.CreateModel(
            name='HighPotentialOpportunityDetailPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('heading', models.CharField(max_length=255)),
                ('contact_proposition', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('contact_button', models.CharField(max_length=500)),
                ('proposition_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_title', models.CharField(max_length=300)),
                ('opportunity_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('opportunity_list_item_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_two_list_item_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competative_advantages_title', models.CharField(max_length=300)),
                ('competative_advantages_list_item_one', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competative_advantages_list_item_two', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('competative_advantages_list_item_three', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('testimonial', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('companies_list_text', core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('case_study_list_title', models.CharField(max_length=300)),
                ('case_study_one_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_two_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_three_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_four_text', core.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('case_study_four_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_one_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_three_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('case_study_two_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_eight', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_five', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_four', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_seven', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_six', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('companies_list_item_image_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('opportunity_list_image', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_one_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_one_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media')),
                ('proposition_two_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('proposition_two_video', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RenameModel(
            old_name='HighPotentialOfferFormPage',
            new_name='HighPotentialOpportunityFormPage',
        ),
    ]