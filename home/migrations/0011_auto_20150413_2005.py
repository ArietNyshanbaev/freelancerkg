# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20150413_2003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillofuser',
            name='level',
            field=models.CharField(default='новичок', choices=[('новичок', 'новичок'), ('продвинутый', 'продвинутый'), ('опытный', 'опытный'), ('эксперт', 'эксперт')], max_length=11),
            preserve_default=True,
        ),
    ]
