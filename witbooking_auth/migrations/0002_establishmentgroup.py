# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0003_auto_20150316_1322'),
        ('witbooking_auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstablishmentGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='establishment')),
                ('establishments', models.ManyToManyField(to='accounting.Establishment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
