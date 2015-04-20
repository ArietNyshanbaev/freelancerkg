# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150323_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skillofuser',
            name='level',
            field=models.CharField(default='новичок', max_length=3, choices=[('новичок', 'Beginner'), ('продвинутый', 'Intermediate'), ('опытный', 'Advanced'), ('эксперт', 'Expert')]),
            preserve_default=True,
        ),
    ]
