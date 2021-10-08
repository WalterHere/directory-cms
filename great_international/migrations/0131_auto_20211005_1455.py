# Generated by Django 2.2.24 on 2021-10-05 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('great_international', '0130_auto_20211005_1005'),
    ]

    operations = [
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='internationalhomepage',
            name='hero_video_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
    ]
