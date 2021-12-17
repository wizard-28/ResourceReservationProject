# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-29 13:40
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_add_ical_token'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='preferred_language',
            field=models.CharField(blank=True, choices=[('fi', 'Finnish'), ('en', 'English'), ('sv', 'Swedish')], max_length=8, null=True, verbose_name='Preferred UI language'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=30, unique=True, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.')], verbose_name='username'),
        ),
    ]
