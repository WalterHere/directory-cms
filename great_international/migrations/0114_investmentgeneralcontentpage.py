# Generated by Django 2.2.24 on 2021-09-14 13:13

import wagtailmarkdown.fields
from django.db import migrations, models
import django.db.models.deletion
import great_international.blocks.great_international
import great_international.panels.investment_atlas
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0059_apply_collection_ordering'),
        ('wagtailimages', '0022_uploadedimage'),
        ('great_international', '0113_sector_page_downpage_content_streamblock_change'),
    ]

    operations = [
        migrations.CreateModel(
            name='InvestmentGeneralContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest'), ('COMPONENTS', 'Components'), ('GREAT_INTERNATIONAL', 'Great International')], db_index=True, max_length=100, null=True)),
                ('uses_tree_based_routing', models.BooleanField(default=False, help_text="Allow this page's URL to be determined by its slug, and the slugs of its ancestors in the page tree.", verbose_name='tree-based routing enabled')),
                ('strapline', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200)),
                ('strapline_en_gb', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_de', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_ja', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_zh_hans', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_fr', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_es', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_pt', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('strapline_ar', models.CharField(help_text='A single sentence which goes beneath the page title', max_length=200, null=True)),
                ('introduction', wagtailmarkdown.fields.MarkdownField()),
                ('introduction_en_gb', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_de', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_ja', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_zh_hans', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_fr', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_es', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_pt', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('introduction_ar', wagtailmarkdown.fields.MarkdownField(null=True)),
                ('main_content', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_en_gb', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_de', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_ja', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_zh_hans', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_fr', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_es', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_pt', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('main_content_ar', wagtail.fields.StreamField([('content_section', wagtail.blocks.StructBlock([('content', wagtail.blocks.StreamBlock([('header', wagtail.blocks.CharBlock(max_length=255, required=False)), ('nested_content', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('text', great_international.blocks.great_international.MarkdownBlock(required=False)), ('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=False)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=False)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))], required=False))], help_text='Use H3 headers or lower, not H2 or H1')), ('columns', wagtail.blocks.StreamBlock([('text', great_international.blocks.great_international.MarkdownBlock())])), ('cta', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False))], min_num=1))], required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text="Only needed if special styling is involved: check with a developer. If in doubt, it's not needed", max_length=255, required=False))]))], blank=True, null=True)),
                ('hero_image', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_ar', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_de', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_en_gb', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_es', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_fr', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_ja', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_pt', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('hero_image_zh_hans', models.ForeignKey(blank=True, help_text='Main page hero image, above the opportunity title', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_ar', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_de', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_en_gb', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_es', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_fr', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_ja', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_pt', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
                ('intro_image_zh_hans', models.ForeignKey(blank=True, help_text='Goes beside the opportunity intro text', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(great_international.panels.investment_atlas.InvestmentGeneralContentPagePanels, 'wagtailcore.page'),
        ),
    ]
