# Generated by Django 2.2.24 on 2021-10-13 15:36

import core.blocks
from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmedia', '0003_copy_media_permissions_to_collections'),
        ('great_international', '0138_auto_20211012_1158'),
    ]

    operations = [
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_ar',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_de',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_en_gb',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_es',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_fr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_ja',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_pt',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AddField(
            model_name='investmentgeneralcontentpage',
            name='hero_video_zh_hans',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailmedia.Media'),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_ar',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_de',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_en_gb',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_es',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_fr',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_ja',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_pt',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='investmentatlaslandingpage',
            name='downpage_sections_zh_hans',
            field=wagtail.fields.StreamField([('panel', wagtail.blocks.StructBlock([('heading', wagtail.blocks.CharBlock(max_length=255, required=True)), ('main_text', wagtail.blocks.TextBlock(help_text='The first column of the panel')), ('call_to_action', wagtail.blocks.StructBlock([('label', wagtail.blocks.CharBlock(max_length=255, required=False)), ('link', wagtail.blocks.StructBlock([('internal_link', wagtail.blocks.PageChooserBlock(label='Internal link', required=False)), ('external_link', wagtail.blocks.CharBlock(label='External link', max_length=255, required=False))], required=False))], help_text='Set text for the CTA and either an internal or an external URL for its destination', required=False)), ('second_column', wagtail.blocks.StreamBlock([('image', wagtail.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(required=True)), ('image_alt', wagtail.blocks.CharBlock(max_length=255, required=True)), ('caption', wagtail.blocks.CharBlock(max_length=255, required=False))])), ('text', wagtail.blocks.TextBlock()), ('video', core.blocks.GreatMediaBlock())], help_text='An image OR a text block, but not both.', label='Second column of panel', max_num=1, required=False)), ('block_slug', wagtail.blocks.CharBlock(help_text='If a block has special content, this helps us identify it. Consult with a developer when you set it. If in doubt, leave it blank.', max_length=255, required=False))], help_text="If 'Block slug' is set to 'with-regions-map', the panel will show the regions map"))], blank=True, null=True),
        ),
    ]
