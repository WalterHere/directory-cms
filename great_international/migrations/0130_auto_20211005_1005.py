# Generated by Django 2.2.24 on 2021-10-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0129_auto_20211004_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.'),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_ar',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_de',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_en_gb',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_es',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_fr',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_ja',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_pt',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
        migrations.AlterField(
            model_name='investmentopportunitypage',
            name='opportunity_summary_zh_hans',
            field=models.TextField(help_text='Simple summary of the Opportunity, for display on OTHER pages (eg listing pages) which link TO a full page about this opportunity. 300 chars max.', null=True),
        ),
    ]
