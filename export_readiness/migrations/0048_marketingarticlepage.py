# Generated by Django 2.2.2 on 2019-06-26 11:51

import core.mixins
import core.model_fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
        ('wagtailimages', '0001_squashed_0021'),
        ('export_readiness', '0047_correct_page_contenttypes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('article_title', models.CharField(max_length=255)),
                ('article_teaser', models.CharField(blank=True, max_length=255, null=True)),
                ('article_body_text', core.model_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('cta_title', models.CharField(blank=True, max_length=255, verbose_name='CTA title')),
                ('cta_teaser', models.TextField(blank=True, verbose_name='CTA teaser')),
                ('cta_link_label', models.CharField(blank=True, max_length=255, verbose_name='CTA link label')),
                ('cta_link', models.CharField(blank=True, max_length=255, verbose_name='CTA link')),
                ('article_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('related_page_one', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('related_page_three', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('related_page_two', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailcore.Page')),
                ('tags', modelcluster.fields.ParentalManyToManyField(blank=True, to='export_readiness.Tag')),
            ],
            options={
                'verbose_name': 'Marketing Article Page',
                'verbose_name_plural': 'Marketing Article Pages',
            },
            bases=(core.mixins.ServiceNameUniqueSlugMixin, 'wagtailcore.page'),
        ),
    ]
