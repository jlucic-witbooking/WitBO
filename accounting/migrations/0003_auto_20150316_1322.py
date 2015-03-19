# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_manual'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aplicaciones',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('identificador', models.CharField(max_length=45, blank=True)),
            ],
            options={
                'db_table': 'aplicaciones',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PartnersTipos',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'partners_tipos',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Reservas',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('fechaentrada', models.DateField()),
                ('fechasalida', models.DateField()),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('telefono', models.CharField(max_length=50, blank=True)),
                ('estado', models.CharField(max_length=10)),
                ('estadoampliado', models.IntegerField()),
                ('habitaciones', models.IntegerField()),
                ('noches', models.IntegerField()),
                ('capacidad', models.IntegerField()),
                ('bebes', models.IntegerField(null=True, blank=True)),
                ('importe', models.DecimalField(max_digits=20, decimal_places=4)),
                ('divisa', models.CharField(max_length=5, blank=True)),
                ('resumen', models.TextField(blank=True)),
                ('idgeneradomulti', models.CharField(max_length=255)),
                ('idgenerado', models.CharField(max_length=20)),
                ('ccnumber', models.CharField(max_length=50)),
                ('ccholder', models.CharField(max_length=50)),
                ('ccvalidto', models.CharField(max_length=50)),
                ('cckind', models.CharField(max_length=50)),
                ('ccsecuritycode', models.CharField(max_length=50, blank=True)),
                ('timestamp', models.DateTimeField()),
                ('tipohab', models.CharField(max_length=25, blank=True)),
                ('tiposhabs_id', models.IntegerField(null=True, blank=True)),
                ('tid', models.CharField(max_length=64, blank=True)),
                ('idafiliado', models.CharField(max_length=255, blank=True)),
                ('idafiliadoreducido', models.CharField(max_length=255, blank=True)),
                ('importepago', models.DecimalField(max_digits=20, decimal_places=4)),
                ('prcjpago', models.DecimalField(max_digits=12, decimal_places=7)),
                ('depositofijo', models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)),
                ('sistemapago_id', models.IntegerField(null=True, blank=True)),
                ('ip', models.CharField(max_length=255, blank=True)),
                ('googleanalyticsok', models.IntegerField(null=True, blank=True)),
                ('idioma', models.CharField(max_length=3, blank=True)),
                ('pais', models.CharField(max_length=255, blank=True)),
                ('tickermotor', models.CharField(max_length=255, blank=True)),
                ('foreign_key', models.IntegerField()),
                ('ultimamodificacion', models.DateTimeField(null=True, blank=True)),
                ('agente_id', models.IntegerField(null=True, blank=True)),
                ('motivocancelacion', models.TextField(blank=True)),
                ('f_cancelacion', models.DateTimeField(null=True, blank=True)),
                ('emailing', models.IntegerField(null=True, blank=True)),
                ('fenvio_encuesta_post_estancia', models.DateField(null=True, blank=True)),
                ('es_consultada_ws', models.IntegerField()),
                ('es_solicita_cancelacion', models.IntegerField()),
                ('control_confirmadas', models.CharField(max_length=255, blank=True)),
                ('es_cancelada_usuario', models.IntegerField()),
                ('es_diferencia_facturadas', models.IntegerField()),
                ('prcj_impuestos', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('importe_promos_sin_impuestos', models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)),
                ('prcj_promos', models.DecimalField(null=True, max_digits=12, decimal_places=7, blank=True)),
                ('importe_aloj_sin_impuestos', models.DecimalField(null=True, max_digits=20, decimal_places=4, blank=True)),
                ('codigo_aplicado', models.CharField(max_length=255, blank=True)),
                ('tracking_trivago', models.CharField(max_length=255, blank=True)),
                ('es_sincronizada', models.IntegerField()),
            ],
            options={
                'db_table': 'reservas',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('identificador', models.CharField(max_length=255)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('password', models.CharField(max_length=40)),
                ('group_id', models.IntegerField()),
                ('creacion', models.DateTimeField(null=True, blank=True)),
                ('modificacion', models.DateTimeField(null=True, blank=True)),
                ('foreign_key', models.IntegerField()),
                ('eliminar', models.IntegerField()),
                ('superusuario', models.IntegerField()),
                ('created', models.DateTimeField(null=True, blank=True)),
                ('modified', models.DateTimeField(null=True, blank=True)),
            ],
            options={
                'db_table': 'users',
                'managed': True,
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='partners',
            name='tipo_partner',
        ),
        migrations.AddField(
            model_name='establishment',
            name='active_transfers',
            field=models.CharField(max_length=255, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='establishment',
            name='aplicacion',
            field=models.ForeignKey(blank=True, to='accounting.Aplicaciones', null=True),
            preserve_default=True,
        ),
    ]
