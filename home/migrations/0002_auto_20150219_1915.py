# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='born_date',
            field=models.DateField(blank=True, default=datetime.datetime.now),
            preserve_default=True,
        ),
    ]
