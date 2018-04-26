# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-12 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('find_a_supplier', '0036_auto_20180410_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryPageArticleSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('industry_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('video', models.URLField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LandingPageArticleSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('industry_name', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('body', wagtail.wagtailcore.fields.RichTextField()),
                ('video', models.URLField(blank=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_five',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_four',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_one',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_six',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_three',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='article_two',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_five',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_four',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_one',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_six',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_three',
        ),
        migrations.RemoveField(
            model_name='landingpage',
            name='article_two',
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_ar',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_de',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_en_gb',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_es',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_fr',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_ja',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_pt',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_pt_br',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_ru',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='landingpagearticlesummary',
            name='page_zh_hans',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.LandingPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_ar',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_de',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_en_gb',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_es',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_fr',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_ja',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_pt',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_pt_br',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_ru',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
        migrations.AddField(
            model_name='industrypagearticlesummary',
            name='page_zh_hans',
            field=modelcluster.fields.ParentalKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='article_summaries', to='find_a_supplier.IndustryPage'),
        ),
    ]