# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('witbooking_auth', '0003_auto_20150319_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='witbookingpermission',
            name='establishment',
            field=models.ForeignKey(to='accounting.Establishment'),
            preserve_default=True,
        ),
    ]
