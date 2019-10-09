# Generated by Django 2.2.4 on 2019-10-09 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('export_readiness', '0062_industrytag_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='questions',
        ),
        migrations.RemoveField(
            model_name='homepage',
            name='questions_section_title',
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_content',
            field=models.TextField(blank=True, null=True, verbose_name='Content'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_cta_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CTA text'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_cta_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='CTA URL'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image', verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_image_alt',
            field=models.TextField(blank=True, null=True, verbose_name='Image alt text'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='madb_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Title'),
        ),
    ]
