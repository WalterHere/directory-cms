# Generated by Django 2.2.4 on 2019-08-27 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('export_readiness', '0052_auto_20190823_1036'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlepage',
            name='article_subheading',
            field=models.TextField(blank=True, help_text='This is a subheading that displays below the main title on the article page'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='article_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='cta_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='cta_link_label',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA link label'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='cta_teaser',
            field=models.TextField(blank=True, verbose_name='CTA teaser'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='cta_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='CTA title'),
        ),
        migrations.AddField(
            model_name='articlepage',
            name='type_of_article',
            field=models.TextField(choices=[('blog', 'Blog'), ('advice', 'Advice'), ('case_study', 'Case study'), ('campaign', 'Campaign')], null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='article_teaser',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='article_title',
            field=models.TextField(),
        ),
    ]