# Generated by Django 2.2.24 on 2021-12-14 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('great_international', '0147_auto_20211214_1025'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InternationalGuideLandingPage',
        ),
    ]
