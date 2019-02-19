# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-06 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('export_readiness', '0047_allcontactpagespage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allcontactpagespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articlelistingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='campaignpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactsuccesspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactsuccesspages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactusguidancepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactusguidancepages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='countryguidepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitdomesticformpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitformpages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitformsuccesspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='euexitinternationalformpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='exportreadinessapp',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='getfinancepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='internationallandingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='marketingpages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardnotespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='performancedashboardpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='privacyandcookiespage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='sitepolicypages',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='termsandconditionspage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='topiclandingpage',
            name='service_name',
            field=models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True),
        ),
    ]