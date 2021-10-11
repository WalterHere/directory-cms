# Generated by Django 2.2.24 on 2021-10-01 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0126_increase_char_limit_for_investmenttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_ar',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_de',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_en_gb',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_es',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_fr',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_ja',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_pt',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='aboutukregionpage',
            name='case_study_text_zh_hans',
            field=models.TextField(blank=True, null=True),
        ),
    ]