# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-15 09:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='host',
            options={'ordering': ['update_time'], 'verbose_name': '\u4e3b\u673a', 'verbose_name_plural': '\u4e3b\u673a'},
        ),
    ]
