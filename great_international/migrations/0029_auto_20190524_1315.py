# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-24 13:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0028_auto_20190524_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='RelatedRegions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_five_zh_hans',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_four_zh_hans',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_one_zh_hans',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_six_zh_hans',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_three_zh_hans',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_ar',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_de',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_en_gb',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_es',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_fr',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_ja',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_pt',
        ),
        migrations.RemoveField(
            model_name='internationalcapitalinvestlandingpage',
            name='related_region_two_zh_hans',
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description',
            field=models.TextField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_ar',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_de',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_en_gb',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_es',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_fr',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_ja',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_pt',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='capitalinvestregionpage',
            name='featured_description_zh_hans',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_ar',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_de',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_en_gb',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_es',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_fr',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_ja',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_pt',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='page_zh_hans',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='added_regions', to='great_international.InternationalCapitalInvestLandingPage'),
        ),
        migrations.AddField(
            model_name='relatedregions',
            name='related_region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='great_international.CapitalInvestRegionPage'),
        ),
    ]
