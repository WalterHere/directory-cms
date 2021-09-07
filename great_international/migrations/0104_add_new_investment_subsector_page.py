# Generated by Django 2.2.24 on 2021-09-07 11:27

from django.db import migrations, models
import django.db.models.deletion
import great_international.panels.great_international


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('great_international', '0103_add_early_opportunities_header_field_to_new_sector_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalInvestmentSubSectorPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('heading', models.CharField(max_length=255, verbose_name='Sub-sector name')),
                ('heading_en_gb', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_de', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_ja', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_zh_hans', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_fr', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_es', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_pt', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
                ('heading_ar', models.CharField(max_length=255, null=True, verbose_name='Sub-sector name')),
            ],
            options={
                'abstract': False,
            },
            bases=(great_international.panels.great_international.InternationalInvestmentSubSectorPagePanels, 'wagtailcore.page'),
        ),
    ]
