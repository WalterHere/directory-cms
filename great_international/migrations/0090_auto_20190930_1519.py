# Generated by Django 2.2.4 on 2019-09-30 15:19

import wagtailmarkdown.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('great_international', '0089_auto_20190926_1031'),
    ]

    operations = [
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_intro_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_four_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_one_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_three_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two',
            field=wagtailmarkdown.fields.MarkdownField(blank=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_text_two_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_four_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_one_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_three_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_ar',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_de',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_es',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_fr',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_ja',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_pt',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_two_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='how_to_expand_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link',
            field=models.CharField(blank=True, max_length=255, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_de',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_ja',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_pt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_link_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta link'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text',
            field=models.CharField(blank=True, max_length=255, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_de',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_ja',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_pt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_cta_text_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section cta text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_ar',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_de',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_en_gb',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_es',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_fr',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_ja',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_pt',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_text_zh_hans',
            field=wagtailmarkdown.fields.MarkdownField(blank=True, null=True, verbose_name='Investment Support Directory section text'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title',
            field=models.CharField(blank=True, max_length=255, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_ar',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_de',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_en_gb',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_es',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_fr',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_ja',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_pt',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AddField(
            model_name='investinternationalhomepage',
            name='isd_section_title_zh_hans',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Investment Support Directory section title'),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text',
            field=models.CharField(blank=True, default='See more industries', max_length=255),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_ar',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_de',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_en_gb',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_es',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_fr',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_ja',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_pt',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='investinternationalhomepage',
            name='sector_button_text_zh_hans',
            field=models.CharField(blank=True, default='See more industries', max_length=255, null=True),
        ),
    ]
