# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20150323_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='category',
            field=models.ForeignKey(default=None, to='home.Category'),
            preserve_default=True,
        ),
    ]
