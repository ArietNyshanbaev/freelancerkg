# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_information_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='stuff',
            field=models.BooleanField(default=False, verbose_name=b'\xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c'),
            preserve_default=True,
        ),
    ]
