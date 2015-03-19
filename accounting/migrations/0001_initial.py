# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
'''
    This commands must be executed for django to ignore pre-existing models

    inspectdb --database=witmetadata > management/models.py
    migrate management --database=witmetadata 0001 --fake
    migrate management --database=witmetadata

'''

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partners',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('ticker', models.CharField(max_length=12)),
                ('direccion', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'db_table': 'partners',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Establishment',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('identificador', models.CharField(unique=True, max_length=255, blank=True)),
                ('alta', models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)),
                ('comi', models.DecimalField(null=True, max_digits=7, decimal_places=4, blank=True)),
                ('comi_neto', models.DecimalField(max_digits=7, decimal_places=4)),
                ('impuestos_neto', models.DecimalField(max_digits=5, decimal_places=2)),
                ('comi_partner', models.DecimalField(null=True, max_digits=7, decimal_places=4, blank=True)),
                ('factura', models.CharField(max_length=255, blank=True)),
                ('fijo_mes', models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)),
                ('cobro_meses', models.IntegerField(null=True, blank=True)),
                ('es_cobro_pre', models.IntegerField(null=True, blank=True)),
                ('cobro_forma', models.CharField(max_length=3, blank=True)),
                ('min', models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)),
                ('min_periodo', models.IntegerField(null=True, blank=True)),
                ('max', models.DecimalField(null=True, max_digits=11, decimal_places=4, blank=True)),
                ('max_periodo', models.IntegerField(null=True, blank=True)),
                ('partner', models.CharField(max_length=255, blank=True)),
                ('partner_id', models.IntegerField(null=True, blank=True)),
                ('es_demo', models.IntegerField(null=True, blank=True)),
                ('es_pruebas', models.IntegerField()),
                ('es_contrato', models.IntegerField()),
                ('fini_actividad', models.DateField(null=True, blank=True)),
                ('fini_actividad_max', models.DateField(null=True, blank=True)),
                ('ffin_actividad', models.DateField(null=True, blank=True)),
                ('es_desactivado', models.IntegerField()),
                ('grupo', models.CharField(max_length=255, blank=True)),
                ('contrato', models.CharField(max_length=255, blank=True)),
                ('max_dias_reserva_modificable', models.IntegerField()),
                ('creacion', models.DateTimeField(null=True, blank=True)),
                ('modificacion', models.DateTimeField(null=True, blank=True)),
                ('version', models.CharField(max_length=20, blank=True)),
                ('es_agregado', models.IntegerField(null=True, blank=True)),
                ('divisa_motor', models.CharField(max_length=3, blank=True)),
                ('ultima_consulta', models.DateTimeField(null=True, blank=True)),
                ('es_agregador_dummy', models.IntegerField()),
            ],
            options={
                'db_table': 'instanciasaplicaciones',
                'managed': True,
            },
            bases=(models.Model,),
        ),
    ]