# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Aplicaciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificador = models.CharField(max_length=45, blank=True)

    def __unicode__(self):
        return u'%s' % self.identificador

    class Meta:
        managed = True
        db_table = 'aplicaciones'

class Client(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cif = models.CharField(max_length=255)
    alias = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=255)
    vat_pct = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    admin_contact = models.CharField(max_length=255)
    admin_phone = models.CharField(max_length=255)
    admin_email = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    collection_currency = models.CharField(max_length=4)

    class Meta:
        managed = True
        db_table = 'client'


class Contract(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    requested_by = models.CharField(max_length=255)
    requested_at = models.DateField()
    start = models.DateField()
    end = models.DateField()
    month_duration = models.IntegerField()
    currency = models.CharField(max_length=4)
    fixed_monthly = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    fixed_quantity = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    commission_pct = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    commission_base = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    commission_partner = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    commission_date_criteria = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    commission_monthly_minimum = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    setup_fee = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    instance = models.ForeignKey('Establishment', blank=True, null=True)
    service = models.ForeignKey('Service')

    class Meta:
        managed = True
        db_table = 'contract'


class Establishment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    aplicacion = models.ForeignKey(Aplicaciones, blank=True, null=True)
    identificador = models.CharField(unique=True, max_length=255, blank=True)
    alta = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    comi = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    comi_neto = models.DecimalField(max_digits=7, decimal_places=4)
    impuestos_neto = models.DecimalField(max_digits=5, decimal_places=2)
    comi_partner = models.DecimalField(max_digits=7, decimal_places=4, blank=True, null=True)
    factura = models.CharField(max_length=255, blank=True)
    fijo_mes = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    cobro_meses = models.IntegerField(blank=True, null=True)
    es_cobro_pre = models.IntegerField(blank=True, null=True)
    cobro_forma = models.CharField(max_length=3, blank=True)
    min = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    min_periodo = models.IntegerField(blank=True, null=True)
    max = models.DecimalField(max_digits=11, decimal_places=4, blank=True, null=True)
    max_periodo = models.IntegerField(blank=True, null=True)
    partner = models.CharField(max_length=255, blank=True)
    partner_id = models.IntegerField(blank=True, null=True)
    es_demo = models.IntegerField(blank=True, null=True)
    es_pruebas = models.IntegerField()
    es_contrato = models.IntegerField()
    fini_actividad = models.DateField(blank=True, null=True)
    ffin_actividad = models.DateField(blank=True, null=True)
    es_desactivado = models.IntegerField()
    grupo = models.CharField(max_length=255, blank=True)
    contrato = models.CharField(max_length=255, blank=True)
    max_dias_reserva_modificable = models.IntegerField()
    creacion = models.DateTimeField(blank=True, null=True)
    modificacion = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=20, blank=True)
    es_agregado = models.IntegerField(blank=True, null=True)
    divisa_motor = models.CharField(max_length=3, blank=True)
    ultima_consulta = models.DateTimeField(blank=True, null=True)
    es_agregador_dummy = models.IntegerField()
    active_transfers = models.CharField(max_length=255, blank=True)
    partner_comercial = models.ForeignKey('Partners', blank=True, null=True, related_name="partner_comercial")
    partner_support = models.ForeignKey('Partners', blank=True, null=True, related_name="partner_support")
    client = models.ForeignKey(Client, blank=True, null=True)
    fini_actividad_max = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return u'%s' % self.identificador

    class Meta:
        managed = True
        db_table = 'instanciasaplicaciones'


class Partners(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)
    ticker = models.CharField(max_length=12)
    direccion = models.CharField(max_length=255, blank=True)
    partner_type = models.CharField(max_length=255, blank=True, null=True)
    margin_pct = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    support_phone = models.CharField(max_length=255, blank=True, null=True)
    support_email = models.CharField(max_length=255, blank=True, null=True)
    support_web = models.CharField(max_length=255, blank=True, null=True)
    support_chat = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'partners'


class PartnersTipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'partners_tipos'


class Reservas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fechaentrada = models.DateField()
    fechasalida = models.DateField()
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50, blank=True)
    estado = models.CharField(max_length=10)
    estadoampliado = models.IntegerField()
    habitaciones = models.IntegerField()
    noches = models.IntegerField()
    capacidad = models.IntegerField()
    bebes = models.IntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=20, decimal_places=4)
    divisa = models.CharField(max_length=5, blank=True)
    resumen = models.TextField(blank=True)
    idgeneradomulti = models.CharField(max_length=255)
    idgenerado = models.CharField(max_length=20)
    ccnumber = models.CharField(max_length=50)
    ccholder = models.CharField(max_length=50)
    ccvalidto = models.CharField(max_length=50)
    cckind = models.CharField(max_length=50)
    ccsecuritycode = models.CharField(max_length=50, blank=True)
    timestamp = models.DateTimeField()
    tipohab = models.CharField(max_length=25, blank=True)
    tiposhabs_id = models.IntegerField(blank=True, null=True)
    tid = models.CharField(max_length=64, blank=True)
    idafiliado = models.CharField(max_length=255, blank=True)
    idafiliadoreducido = models.CharField(max_length=255, blank=True)
    importepago = models.DecimalField(max_digits=20, decimal_places=4)
    prcjpago = models.DecimalField(max_digits=12, decimal_places=7)
    depositofijo = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    sistemapago_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True)
    googleanalyticsok = models.IntegerField(blank=True, null=True)
    idioma = models.CharField(max_length=3, blank=True)
    pais = models.CharField(max_length=255, blank=True)
    tickermotor = models.CharField(max_length=255, blank=True)
    foreign_key = models.IntegerField()
    ultimamodificacion = models.DateTimeField(blank=True, null=True)
    agente_id = models.IntegerField(blank=True, null=True)
    motivocancelacion = models.TextField(blank=True)
    f_cancelacion = models.DateTimeField(blank=True, null=True)
    emailing = models.IntegerField(blank=True, null=True)
    fenvio_encuesta_post_estancia = models.DateField(blank=True, null=True)
    es_consultada_ws = models.IntegerField()
    es_solicita_cancelacion = models.IntegerField()
    control_confirmadas = models.CharField(max_length=255, blank=True)
    es_cancelada_usuario = models.IntegerField()
    es_diferencia_facturadas = models.IntegerField()
    prcj_impuestos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_promos_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    prcj_promos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_aloj_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    codigo_aplicado = models.CharField(max_length=255, blank=True)
    tracking_trivago = models.CharField(max_length=255, blank=True)
    es_sincronizada = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'reservas'


class Service(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=255)
    margin_pct = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'service'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    identificador = models.CharField(max_length=255)
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=40)
    group_id = models.IntegerField()
    creacion = models.DateTimeField(blank=True, null=True)
    modificacion = models.DateTimeField(blank=True, null=True)
    foreign_key = models.IntegerField()
    eliminar = models.IntegerField()
    superusuario = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'users'

