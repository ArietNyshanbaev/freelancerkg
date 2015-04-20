# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_information_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='category',
            field=models.ForeignKey(to='home.Category'),
            preserve_default=True,
        ),
    ]
