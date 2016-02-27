# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attapi', '0007_auto_20160227_1946'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('learner_user', models.ForeignKey(related_name='learner_notification', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(to='attapi.Subject')),
                ('tutor_user', models.ForeignKey(related_name='tutor_notification', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
