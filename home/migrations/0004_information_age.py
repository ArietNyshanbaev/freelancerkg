# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_information_stuff'),
    ]

    operations = [
        migrations.AddField(
            model_name='information',
            name='age',
            field=models.IntegerField(null=True, verbose_name=b'\xd0\xb2\xd0\xbe\xd0\xb7\xd1\x80\xd0\xb0\xd1\x81\xd1\x82', blank=True),
            preserve_default=True,
        ),
    ]
