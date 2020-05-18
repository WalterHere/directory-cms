# Generated by Django 2.2.10 on 2020-05-18 09:16

import core.model_fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0073_auto_20200203_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='data_description_row_three',
            field=core.model_fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='data_number_row_three',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='data_period_row_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='data_title_row_three',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
