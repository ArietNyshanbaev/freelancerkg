# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150624_0351'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='note_for_us',
            field=models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x81', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='information',
            name='note_of_pirces',
            field=models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x85 \xd0\xb8 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x85', blank=True),
            preserve_default=True,
        ),
    ]
