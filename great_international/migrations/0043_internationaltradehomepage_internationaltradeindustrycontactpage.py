# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-06-18 10:48
from __future__ import unicode_literals

import core.mixins
import wagtailmarkdown.fields
import core.models
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
        ('great_international', '0042_auto_20190617_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalTradeHomePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('hero_image_caption', models.CharField(blank=True, max_length=255)),
                ('hero_image_caption_en_gb', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_de', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_ja', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_zh_hans', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_fr', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_es', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_pt', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image_caption_ar', models.CharField(blank=True, max_length=255, null=True)),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('breadcrumbs_label_en_gb', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_de', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_ja', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_zh_hans', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_fr', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_es', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_pt', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_ar', models.CharField(max_length=50, null=True)),
                ('hero_text', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('hero_text_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_text_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('search_field_placeholder', models.CharField(max_length=500)),
                ('search_field_placeholder_en_gb', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_de', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_ja', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_zh_hans', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_fr', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_es', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_pt', models.CharField(max_length=500, null=True)),
                ('search_field_placeholder_ar', models.CharField(max_length=500, null=True)),
                ('search_button_text', models.CharField(max_length=500)),
                ('search_button_text_en_gb', models.CharField(max_length=500, null=True)),
                ('search_button_text_de', models.CharField(max_length=500, null=True)),
                ('search_button_text_ja', models.CharField(max_length=500, null=True)),
                ('search_button_text_zh_hans', models.CharField(max_length=500, null=True)),
                ('search_button_text_fr', models.CharField(max_length=500, null=True)),
                ('search_button_text_es', models.CharField(max_length=500, null=True)),
                ('search_button_text_pt', models.CharField(max_length=500, null=True)),
                ('search_button_text_ar', models.CharField(max_length=500, null=True)),
                ('proposition_text', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('proposition_text_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('call_to_action_text', models.CharField(max_length=500)),
                ('call_to_action_text_en_gb', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_de', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_ja', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_zh_hans', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_fr', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_es', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_pt', models.CharField(max_length=500, null=True)),
                ('call_to_action_text_ar', models.CharField(max_length=500, null=True)),
                ('industries_list_text', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_text_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('industries_list_call_to_action_text', models.CharField(max_length=500)),
                ('industries_list_call_to_action_text_en_gb', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_de', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_ja', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_zh_hans', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_fr', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_es', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_pt', models.CharField(max_length=500, null=True)),
                ('industries_list_call_to_action_text_ar', models.CharField(max_length=500, null=True)),
                ('services_list_text', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_list_text_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_one_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_two_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_three_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four', wagtailmarkdown.fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_en_gb', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_de', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_ja', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_fr', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_es', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_pt', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('services_column_four_ar', wagtailmarkdown.fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks])),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('mobile_hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_ar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_en_gb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_fr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_ja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_pt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_four_icon_zh_hans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_ar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_en_gb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_fr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_ja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_pt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_one_icon_zh_hans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_ar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_en_gb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_fr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_ja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_pt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_three_icon_zh_hans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_ar', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_de', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_en_gb', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_es', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_fr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_ja', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_pt', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('services_column_two_icon_zh_hans', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, core.mixins.ServiceHomepageMixin, 'wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='InternationalTradeIndustryContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('breadcrumbs_label', models.CharField(max_length=50)),
                ('breadcrumbs_label_en_gb', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_de', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_ja', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_zh_hans', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_fr', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_es', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_pt', models.CharField(max_length=50, null=True)),
                ('breadcrumbs_label_ar', models.CharField(max_length=50, null=True)),
                ('introduction_text', wagtailmarkdown.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_en_gb', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_de', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_ja', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_zh_hans', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_fr', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_es', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_pt', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('introduction_text_ar', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('submit_button_text', models.CharField(max_length=100)),
                ('submit_button_text_en_gb', models.CharField(max_length=100, null=True)),
                ('submit_button_text_de', models.CharField(max_length=100, null=True)),
                ('submit_button_text_ja', models.CharField(max_length=100, null=True)),
                ('submit_button_text_zh_hans', models.CharField(max_length=100, null=True)),
                ('submit_button_text_fr', models.CharField(max_length=100, null=True)),
                ('submit_button_text_es', models.CharField(max_length=100, null=True)),
                ('submit_button_text_pt', models.CharField(max_length=100, null=True)),
                ('submit_button_text_ar', models.CharField(max_length=100, null=True)),
                ('success_message_text', wagtailmarkdown.fields.MarkdownField(blank=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_en_gb', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_de', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_ja', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_zh_hans', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_fr', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_es', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_pt', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_message_text_ar', wagtailmarkdown.fields.MarkdownField(blank=True, null=True, validators=[core.validators.slug_hyperlinks])),
                ('success_back_link_text', models.CharField(max_length=100)),
                ('success_back_link_text_en_gb', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_de', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_ja', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_zh_hans', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_fr', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_es', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_pt', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_ar', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page', models.Model),
        ),
    ]
