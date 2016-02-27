# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attapi', '0003_auto_20160227_1729'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='phone_number',
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='interested_subject',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='location',
            field=models.CharField(max_length=50, default='', blank=True),
        ),
    ]
