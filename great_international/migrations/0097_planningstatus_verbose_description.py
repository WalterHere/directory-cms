# Generated by Django 2.2.24 on 2021-08-30 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('great_international', '0096_auto_20210820_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='planningstatus',
            name='verbose_description',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
