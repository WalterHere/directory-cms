# Generated by Django 2.2.24 on 2021-12-08 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('great_international', '0142_auto_20211208_1532'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CapitalInvestOpportunityListingPage',
        ),
    ]
