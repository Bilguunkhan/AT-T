# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attapi', '0004_auto_20160227_0759'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='is_teacher',
            field=models.CharField(default='', max_length=50, blank=True),
        ),
    ]
