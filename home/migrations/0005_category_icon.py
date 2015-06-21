# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_information_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True),
            preserve_default=True,
        ),
    ]
