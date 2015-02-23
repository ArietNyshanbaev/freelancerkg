# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(upload_to='media')),
                ('gender', models.CharField(default='M', max_length=2, choices=[('M', 'Male'), ('F', 'Female')])),
                ('born_date', models.DateField(auto_now_add=True)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(default='Не указано', max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('category', models.ForeignKey(to='home.Category')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillofUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience', models.IntegerField()),
                ('level', models.CharField(default='BEG', max_length=3, choices=[('BEG', 'Beginner'), ('INM', 'Intermediate'), ('ADV', 'Advanced'), ('EXP', 'Expert')])),
                ('skill', models.ForeignKey(to='home.Skill')),
                ('user', models.ForeignKey(to='home.Information')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
