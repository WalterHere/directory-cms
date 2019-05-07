# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-07 14:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0008_alter_user_username_max_length'),
        ('users', '0002_create_profile_existing_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='self_assigned_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='team_leader',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='team_leader_for', to=settings.AUTH_USER_MODEL),
        ),
    ]
