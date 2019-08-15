# Generated by Django 2.2.3 on 2019-08-14 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0066_capitalinvestcontactformpage_capitalinvestcontactformsuccesspage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page'),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ar',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_de',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_en_gb',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_es',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_fr',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_ja',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_pt',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
        migrations.AlterField(
            model_name='internationalarticlepage',
            name='article_teaser_zh_hans',
            field=models.TextField(blank=True, help_text='This is a subheading that displays when the article is featured on another page', null=True),
        ),
    ]
