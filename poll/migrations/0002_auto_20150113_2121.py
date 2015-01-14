# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='townhallpoll',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name=b'published'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='townhallresponse',
            name='first_name',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='townhallresponse',
            name='last_name',
            field=models.CharField(max_length=120, null=True, blank=True),
            preserve_default=True,
        ),
    ]
