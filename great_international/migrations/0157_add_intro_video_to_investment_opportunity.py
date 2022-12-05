# Generated by Django 2.2.28 on 2022-11-14 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('great_international', '0156_remove_international_eu_exit_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentopportunitypage',
            name='intro_video_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]
