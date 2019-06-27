# Generated by Django 2.2.2 on 2019-06-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0050_auto_20190627_1422'),
    ]

    operations = [
        migrations.AddField(
            model_name='marketingarticlepage',
            name='related_page_one',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage'),
        ),
        migrations.AddField(
            model_name='marketingarticlepage',
            name='related_page_three',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage'),
        ),
        migrations.AddField(
            model_name='marketingarticlepage',
            name='related_page_two',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='export_readiness.ArticlePage'),
        ),
    ]
