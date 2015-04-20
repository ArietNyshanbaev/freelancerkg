# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20150320_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='date',
            field=models.DateField(default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
