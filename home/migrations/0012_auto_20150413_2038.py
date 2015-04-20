# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20150413_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillofuser',
            name='level',
            field=models.CharField(max_length=11),
            preserve_default=True,
        ),
    ]
