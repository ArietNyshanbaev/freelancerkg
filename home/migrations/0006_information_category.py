# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_information_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='category',
            field=models.ForeignKey(to='home.Category', default=None),
            preserve_default=True,
        ),
    ]
