# Generated by Django 2.2.3 on 2019-07-30 13:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('great_international', '0056_auto_20190725_1613'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvestSectorPage',
            new_name='InvestRegionPage',
        ),
    ]