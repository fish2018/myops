# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-15 08:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deploy', '0004_deploydcos_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploydcos',
            name='num',
            field=models.IntegerField(default=1, max_length=1000, verbose_name='\u6784\u5efa\u7f16\u53f7'),
        ),
    ]