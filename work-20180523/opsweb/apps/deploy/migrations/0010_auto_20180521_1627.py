# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-21 08:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0009_deploydcos_buildstatus'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deploydcos',
            options={'ordering': ['-jobname']},
        ),
    ]