# Generated by Django 2.2.24 on 2021-12-14 11:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailforms', '0004_add_verbose_name_plural'),
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('great_international', '0151_auto_20211214_1132'),
    ]

    operations = [
        migrations.DeleteModel(
            name='InvestInternationalHomePage',
        ),
    ]
