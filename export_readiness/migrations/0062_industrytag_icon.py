# Generated by Django 2.2.4 on 2019-09-25 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('export_readiness', '0061_articlepage_article_video_transcript'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrytag',
            name='icon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]