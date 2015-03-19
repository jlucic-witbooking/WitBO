# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('cif', models.CharField(max_length=255)),
                ('alias', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('company_name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('vat_pct', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('admin_contact', models.CharField(max_length=255)),
                ('admin_phone', models.CharField(max_length=255)),
                ('admin_email', models.CharField(max_length=255)),
                ('payment_type', models.CharField(max_length=255)),
                ('collection_currency', models.CharField(max_length=4)),
            ],
            options={
                'db_table': 'client',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('requested_by', models.CharField(max_length=255)),
                ('requested_at', models.DateField()),
                ('start', models.DateField()),
                ('end', models.DateField()),
                ('month_duration', models.IntegerField()),
                ('currency', models.CharField(max_length=4)),
                ('fixed_monthly', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('fixed_quantity', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('commission_pct', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('commission_base', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('commission_partner', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('commission_date_criteria', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('commission_monthly_minimum', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('setup_fee', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
            ],
            options={
                'db_table': 'contract',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('margin_pct', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
            ],
            options={
                'db_table': 'service',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='establishment',
            name='partner_comercial',
            field=models.ForeignKey(related_name='partner_comercial', blank=True, to='accounting.Partners', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='establishment',
            name='partner_support',
            field=models.ForeignKey(related_name='partner_support', blank=True, to='accounting.Partners', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='service',
            field=models.ForeignKey(to='accounting.Service'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='establishment',
            name='client',
            field=models.ForeignKey(blank=True, to='accounting.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='contract',
            name='instance',
            field=models.ForeignKey(blank=True, to='accounting.Establishment', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='tipo_partner',
            field=models.ForeignKey(blank=True, to='accounting.Client', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='partner_type',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='margin_pct',
            field=models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='support_phone',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='support_email',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='support_web',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='Partners',
            name='support_chat',
            field=models.CharField(max_length=255, blank=True, null=True),
            preserve_default=True,
        ),
    ]
