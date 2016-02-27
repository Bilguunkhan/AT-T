# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attapi', '0006_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='learners',
            field=models.ManyToManyField(related_name='learn_subjects', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='subject',
            name='tutors',
            field=models.ManyToManyField(related_name='tutor_subjects', to=settings.AUTH_USER_MODEL),
        ),
    ]
