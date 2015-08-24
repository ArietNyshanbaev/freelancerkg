# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f')),
                ('icon', models.ImageField(upload_to=b'', null=True, verbose_name=b'\xd0\xb8\xd0\xba\xd0\xbe\xd0\xbd\xd0\xba\xd0\xb0', blank=True)),
            ],
            options={
                'verbose_name': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f',
                'verbose_name_plural': '\u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('image', models.ImageField(upload_to=b'media', null=True, verbose_name=b'\xd1\x84\xd0\xbe\xd1\x82\xd0\xbe', blank=True)),
                ('gender', models.CharField(default=b'M', max_length=2, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb', choices=[(b'M', b'Male'), (b'F', b'Female')])),
                ('born_date', models.DateField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xbe\xd0\xb6\xd0\xb4\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f', blank=True)),
                ('phone_number', models.IntegerField(verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8')),
                ('stuff', models.BooleanField(default=False, verbose_name=b'\xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c')),
                ('note', models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5', blank=True)),
                ('note_for_us', models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xb4\xd0\xbb\xd1\x8f \xd0\xbd\xd0\xb0\xd1\x81', blank=True)),
                ('note_of_prices', models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xb8\xd0\xbd\xd1\x84\xd0\xbe\xd1\x80\xd0\xbc\xd0\xb0\xd1\x86\xd0\xb8\xd1\x8f \xd0\xbe \xd0\xb4\xd0\xb5\xd0\xbb\xd0\xb0\xd1\x85 \xd0\xb8 \xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0\xd1\x85', blank=True)),
                ('just_in_case', models.CharField(max_length=3000, null=True, verbose_name=b'\xd0\xbd\xd0\xb0 \xd0\xb2\xd1\x81\xd1\x8f\xd0\xba\xd0\xb8\xd0\xb9 \xd1\x81\xd0\xbb\xd1\x83\xd1\x87\xd0\xb0\xd0\xb9', blank=True)),
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('category', models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='home.Category')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0430\u043d\u043a\u0435\u0442\u0430',
                'verbose_name_plural': '\u0430\u043d\u043a\u0435\u0442\u044b',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('description', models.TextField(null=True, verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5', blank=True)),
                ('price', models.IntegerField(null=True, verbose_name=b'\xd1\x86\xd0\xb5\xd0\xbd\xd0\xb0', blank=True)),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb4\xd0\xbe\xd0\xb1\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
                ('address', models.TextField(null=True, verbose_name=b'\xd0\xb0\xd0\xb4\xd1\x80\xd0\xb5\xd1\x81', blank=True)),
                ('category', models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='home.Category')),
                ('user', models.ForeignKey(default=None, verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': '\u0437\u0430\u0434\u0430\u043d\u0438\u0435',
                'verbose_name_plural': '\u0437\u0430\u0434\u0430\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xb8\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8f')),
                ('email', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, verbose_name=b'\xd1\x82\xd0\xb5\xd0\xbc\xd0\xb0')),
                ('body', models.CharField(max_length=1000, verbose_name=b'\xd1\x81\xd0\xbe\xd0\xbe\xd0\xb1\xd1\x89\xd0\xb5\xd0\xbd\xd0\xb8\xd0\xb5')),
                ('date', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xbe\xd1\x82\xd0\xbf\xd1\x80\xd0\xb0\xd0\xb2\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f')),
            ],
            options={
                'verbose_name': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435',
                'verbose_name_plural': '\u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name=b'\xd0\xb8\xd0\xbc\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd1\x87\xd0\xb8\xd0\xba\xd0\xb0')),
                ('telephone', models.CharField(max_length=100, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('date_of_order', models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=200, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xb8\xd1\x81\xd0\xbf\xd0\xbe\xd0\xbb\xd0\xbd\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('job_description', models.TextField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', verbose_name=b'\xd0\xbe\xd0\xbf\xd0\xb8\xd1\x81\xd0\xb0\xd0\xbd\xd0\xb8\xd0\xb5 \xd0\xb7\xd0\xb0\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0')),
                ('address', models.CharField(default=b'\xd0\xbd\xd0\xb5 \xd1\x83\xd0\xba\xd0\xb0\xd0\xb7\xd0\xb0\xd0\xbd', max_length=400, verbose_name=b'\xd0\xbd\xd0\xbe\xd0\xbc\xd0\xb5\xd1\x80 \xd1\x82\xd0\xb5\xd0\xbb\xd0\xb5\xd1\x84\xd0\xbe\xd0\xbd\xd0\xb0')),
                ('date_of_submition', models.DateTimeField(default=datetime.datetime.now, verbose_name=b'\xd0\xb4\xd0\xb0\xd1\x82\xd0\xb0 \xd0\xb8 \xd0\xb2\xd1\x80\xd0\xb5\xd0\xbc\xd1\x8f \xd0\xbf\xd0\xbe\xd1\x81\xd1\x82\xd1\x83\xd0\xbf\xd0\xbb\xd0\xb5\xd0\xbd\xd0\xb8\xd1\x8f \xd0\xb7\xd0\xb0\xd1\x8f\xd0\xb2\xd0\xba\xd0\xb8')),
                ('category', models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='home.Category')),
            ],
            options={
                'verbose_name': '\u0437\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0437\u0430\u044f\u0432\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba')),
                ('category', models.ForeignKey(verbose_name=b'\xd0\xba\xd0\xb0\xd1\x82\xd0\xb5\xd0\xb3\xd0\xbe\xd1\x80\xd0\xb8\xd1\x8f', to='home.Category')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u0432\u044b\u043a',
                'verbose_name_plural': '\u043d\u0430\u0432\u044b\u043a\u0438',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SkillofUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('experience', models.IntegerField(verbose_name=b'\xd1\x81\xd1\x82\xd0\xb0\xd0\xb6')),
                ('level', models.CharField(max_length=11, verbose_name=b'\xd1\x83\xd1\x80\xd0\xbe\xd0\xb2\xd0\xb5\xd0\xbd\xd1\x8c \xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba\xd0\xb0')),
                ('skill', models.ForeignKey(verbose_name=b'\xd0\xbd\xd0\xb0\xd0\xb2\xd1\x8b\xd0\xba', to='home.Skill')),
                ('user', models.ForeignKey(verbose_name=b'\xd0\xbf\xd0\xbe\xd0\xbb\xd1\x8c\xd0\xb7\xd0\xbe\xd0\xb2\xd0\xb0\xd1\x82\xd0\xb5\xd0\xbb\xd1\x8c', to='home.Information')),
            ],
            options={
                'verbose_name': '\u043d\u0430\u0432\u044b\u043a \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044f',
                'verbose_name_plural': '\u043d\u0430\u0432\u044b\u043a\u0438 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Slogan',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('body', models.CharField(max_length=200, verbose_name=b'\xd1\x86\xd0\xb8\xd1\x82\xd0\xb0\xd1\x82\xd0\xb0')),
            ],
            options={
                'verbose_name': '\u0446\u0438\u0442\u0430\u0442\u0430',
                'verbose_name_plural': '\u0446\u0438\u0442\u0430\u0442\u044b',
            },
            bases=(models.Model,),
        ),
    ]
