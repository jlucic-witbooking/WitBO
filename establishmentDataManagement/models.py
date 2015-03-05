# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
# * Make sure each model has one field with primary_key=True
# * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models

class Acos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True)
    foreign_key = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'acos'


class Adwords(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    clave = models.CharField(max_length=255)
    codigo = models.TextField()
    idioma = models.CharField(max_length=10)
    activo = models.IntegerField()
    modificado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'adwords'


class Agentes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=50, blank=True)
    ticker = models.CharField(max_length=12)
    email = models.CharField(max_length=255, blank=True)
    telefono = models.IntegerField(blank=True, null=True)
    comision = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipotc = models.CharField(max_length=255, blank=True)
    titulartc = models.CharField(max_length=255, blank=True)
    numtc = models.CharField(max_length=255, blank=True)
    mestc = models.IntegerField(blank=True, null=True)
    anyotc = models.IntegerField(blank=True, null=True)
    tipodatostc = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'agentes'


class AlojamientoConfiguraciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=255)
    adultos = models.IntegerField(blank=True, null=True)
    ninos = models.IntegerField(blank=True, null=True)
    bebes = models.IntegerField(blank=True, null=True)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()
    orden = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alojamiento_configuraciones'


class AlojamientoTipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(unique=True, max_length=12)
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    color = models.CharField(max_length=7, blank=True)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()
    deleted = models.IntegerField()
    orden = models.IntegerField()
    visible = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'alojamiento_tipos'


class Anyos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?

    class Meta:
        managed = False
        db_table = 'anyos'


class Apariencias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    idperfilcolor = models.ForeignKey('Perfilescolor', db_column='idPerfilColor', blank=True,
                                      null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'apariencias'


class Aros(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    parent_id = models.IntegerField(blank=True, null=True)
    model = models.CharField(max_length=255, blank=True)
    foreign_key = models.IntegerField(blank=True, null=True)
    alias = models.CharField(max_length=255, blank=True)
    lft = models.IntegerField(blank=True, null=True)
    rght = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'aros'


class ArosAcos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    aro = models.ForeignKey(Aros)
    aco = models.ForeignKey(Acos)
    field_create = models.CharField(db_column='_create', max_length=2)  # Field renamed because it started with '_'.
    field_read = models.CharField(db_column='_read', max_length=2)  # Field renamed because it started with '_'.
    field_update = models.CharField(db_column='_update', max_length=2)  # Field renamed because it started with '_'.
    field_delete = models.CharField(db_column='_delete', max_length=2)  # Field renamed because it started with '_'.

    class Meta:
        managed = False
        db_table = 'aros_acos'


class Caches(models.Model):
    id = models.CharField(primary_key=True, max_length=100)
    conditions = models.TextField()
    content = models.TextField()

    class Meta:
        managed = False
        db_table = 'caches'


class CakeSessions(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    data = models.TextField(blank=True)
    expires = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cake_sessions'


class Channelmanagers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    canal_id = models.IntegerField()
    activo = models.IntegerField()
    markup = models.IntegerField()
    disponibilidad = models.IntegerField()
    impuestos = models.IntegerField()
    editado = models.DateField()

    class Meta:
        managed = False
        db_table = 'channelmanagers'


class ChannelmanagersEquivalencias(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    canal_id = models.IntegerField()
    tiposhab_id = models.IntegerField()
    equivalencia = models.CharField(max_length=90)

    class Meta:
        managed = False
        db_table = 'channelmanagers_equivalencias'


class ChannelsCodeTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    channels_integrations = models.ForeignKey('ChannelsIntegrations', db_column='channels_integrations')
    channels_mappings_code_types = models.ForeignKey('ChannelsMappingsCodeTypes',
                                                     db_column='channels_mappings_code_types')

    class Meta:
        managed = False
        db_table = 'channels_code_types'


class ChannelsIntegrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    channel_ticker = models.CharField(unique=True, max_length=45)
    user = models.CharField(max_length=45, blank=True)
    password = models.CharField(max_length=45, blank=True)
    multiplier = models.FloatField()
    agent_id = models.IntegerField(blank=True, null=True)
    protocol_push = models.IntegerField()
    address_push = models.TextField(blank=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'channels_integrations'


class ChannelsMappings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    channels_integrations = models.ForeignKey(ChannelsIntegrations, db_column='channels_integrations')
    tiposhabs_ticker = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'channels_mappings'


class ChannelsMappingsCodeTypes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=45)

    class Meta:
        managed = False
        db_table = 'channels_mappings_code_types'


class ChannelsMappingsCodes(models.Model):
    id = models.IntegerField(primary_key=True)
    channels_mappings = models.ForeignKey(ChannelsMappings, db_column='channels_mappings')
    value = models.CharField(max_length=45)
    channels_mappings_code_types = models.ForeignKey(ChannelsMappingsCodeTypes,
                                                     db_column='channels_mappings_code_types')

    class Meta:
        managed = False
        db_table = 'channels_mappings_codes'


class Complementos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(max_length=11)
    nombre = models.CharField(max_length=50)
    activo = models.IntegerField()
    orden = models.IntegerField()
    ultimamodif = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'complementos'


class Comunicacionespropiedades(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    clave = models.CharField(max_length=45, blank=True)
    valor = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comunicacionespropiedades'


class Condiciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(max_length=12, blank=True)
    sistemapago = models.ForeignKey('Sistemaspago')
    nombre = models.CharField(max_length=255)
    prcj_deposito = models.DecimalField(max_digits=5, decimal_places=2)
    min_deposito = models.DecimalField(max_digits=10, decimal_places=4)
    min_antelacion_cancelar = models.IntegerField()
    htmlresumen = models.CharField(max_length=45)
    htmlcompleto = models.TextField()
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()
    html_deposito_pago = models.TextField(blank=True)
    html_politica_cancelacion = models.TextField(blank=True)
    html_entradas_salidas = models.TextField(blank=True)
    html_servicios_limpieza = models.TextField(blank=True)
    html_ninyos = models.TextField(blank=True)
    condiciones_apartados = models.ForeignKey('CondicionesApartados')

    class Meta:
        managed = False
        db_table = 'condiciones'


class CondicionesApartados(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    seccion = models.ForeignKey('CondicionesSecciones')
    titulo = models.CharField(max_length=75)
    html = models.TextField(blank=True)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'condiciones_apartados'


class CondicionesSecciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'condiciones_secciones'


class Configuracionessmtps(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(unique=True, max_length=255)
    tipo = models.CharField(max_length=90)
    puerto = models.CharField(max_length=9)
    cuenta = models.CharField(max_length=255, blank=True)
    contrase_a = models.CharField(db_column='contrase\xf1a', max_length=765,
                                  blank=True)  # Field renamed to remove unsuitable characters.
    seguridad = models.CharField(max_length=90)
    nombre_usuario = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'configuracionessmtps'


class Configuracionpropiedades(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    clave = models.CharField(unique=True, max_length=45, blank=True)
    valor = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'configuracionpropiedades'


class Configurations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    apariencia = models.ForeignKey(Apariencias, blank=True, null=True)
    l10ncatalog = models.ForeignKey('L10Ncatalogs', blank=True, null=True)
    title = models.CharField(max_length=2005, blank=True)
    showheadertitle = models.IntegerField()
    keywords = models.TextField(blank=True)
    description = models.TextField(blank=True)
    analyticscode = models.TextField(blank=True)
    googleanalyticscodenumber = models.CharField(max_length=30, blank=True)
    emails = models.CharField(max_length=255)
    charset = models.CharField(max_length=45, blank=True)
    maxdisponibilidad = models.IntegerField(blank=True, null=True)
    maxfecha = models.DateField(blank=True, null=True)
    maxhabitaciones = models.IntegerField(blank=True, null=True)
    config = models.TextField(blank=True)
    activemodules = models.TextField(blank=True)
    lastmodified = models.DateTimeField(blank=True, null=True)
    taxes = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    taxes_inventario = models.DecimalField(max_digits=7, decimal_places=6)
    showrateswithtaxesincluded = models.IntegerField()
    defaultcurrency = models.CharField(max_length=45, blank=True)
    adminemail = models.CharField(max_length=255, blank=True)
    updatepricestaxesincluded = models.IntegerField()
    layouttheme = models.CharField(max_length=255)
    version = models.IntegerField()
    header_colors = models.CharField(max_length=200)
    color_tinactivo_cabecera = models.CharField(max_length=6, blank=True)
    color_tactivo_cabecera = models.CharField(max_length=6, blank=True)
    price_interval = models.CharField(max_length=200)
    roomsbooster = models.IntegerField()
    dtospromosexcluyentes = models.IntegerField()
    mostrarreservamultiple = models.IntegerField()
    mostrarpromociones = models.IntegerField()
    packs = models.IntegerField()
    emaildirector = models.CharField(max_length=255)
    urlwebhotel = models.CharField(max_length=255)
    showlinkbacktohotel = models.IntegerField()
    showhotelmenu = models.IntegerField()
    hotelmenu = models.TextField(blank=True)
    logolinkstohotel = models.IntegerField()
    enviarmensajesdirector = models.IntegerField()
    pedircodigoseguridad = models.IntegerField()
    propiedades = models.TextField()
    activarusos = models.IntegerField()
    activarusospacks = models.IntegerField()
    stockcompartido = models.IntegerField()
    minimodias = models.IntegerField()
    modocargadisponibilidad = models.IntegerField()
    activarcondicionesespecificas = models.IntegerField()
    solicitarrepetiremail = models.IntegerField()
    activarestadasminimas = models.IntegerField()
    ciudad = models.CharField(max_length=50, blank=True)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    mostrarinfoafiliado = models.IntegerField()
    setupterminado = models.IntegerField()
    actualizarporrangos = models.IntegerField()
    setupfinished = models.IntegerField()
    mostrarpaquetesenespeciales = models.IntegerField()
    importeactivartvp = models.DecimalField(max_digits=11, decimal_places=3)
    prcjcobrotpv = models.DecimalField(max_digits=5, decimal_places=4)
    sistemapago = models.IntegerField()
    issinglesignon = models.IntegerField()
    isdesglosetagsenresumen = models.IntegerField(blank=True, null=True)
    ismostrarlistaemails = models.IntegerField(blank=True, null=True)
    isdesglosetags = models.IntegerField(blank=True, null=True)
    isextrastarifavariable = models.IntegerField()
    activarfiltropersonas = models.IntegerField()
    filtroconninos = models.IntegerField()
    minedadnino = models.IntegerField()
    maxedadnino = models.IntegerField()
    cobroanticipadoactivo = models.IntegerField()
    gestionavanzadainventario = models.IntegerField()
    esestminindependientes = models.IntegerField(db_column='esEstMinIndependientes')  # Field name made lowercase.
    activarregimenes = models.IntegerField()
    activarhorizontecalendario = models.IntegerField()
    numdiastarifasvisibles = models.IntegerField(blank=True, null=True)
    numdiashorizontecalendario = models.IntegerField(blank=True, null=True)
    calendariosiemprevisible = models.IntegerField()
    isconfiguracionavanzadacargos = models.IntegerField()
    espromocionesfechacontratacion = models.IntegerField()
    espromocionesvinculadasregimen = models.IntegerField()
    espromocionessoloalojamiento = models.IntegerField()
    espromocionesopcionalesincompatibles = models.IntegerField()
    esformulaalojamiento = models.IntegerField()
    colorcalendario = models.CharField(max_length=6, blank=True)
    esmanejoagregadoreservas = models.IntegerField()
    espromocionesfechaentrada = models.IntegerField()
    espromocionescalculopordia = models.IntegerField()
    es_prom_mostrar_excluidos = models.IntegerField()
    horasrelease = models.IntegerField()
    multipropiedad = models.IntegerField()
    esmostrarnodisponibles = models.IntegerField(blank=True, null=True)
    esbebesactivo = models.IntegerField(blank=True, null=True)
    esbebesgratis = models.IntegerField(blank=True, null=True)
    idiomaemailhotel = models.CharField(max_length=3, blank=True)
    escondicionesemailhotel = models.IntegerField(blank=True, null=True)
    esfechadesglosebono = models.IntegerField(blank=True, null=True)
    escondicionesespeciales = models.IntegerField(blank=True, null=True)
    maxninosminiform = models.IntegerField()
    eslistadosinimpuestos = models.IntegerField()
    escodigodesplegado = models.IntegerField()
    eseditarreservas = models.IntegerField()
    esmultiedadesninos = models.IntegerField(db_column='esMultiEdadesNinos')  # Field name made lowercase.
    nummaxextrasenlista = models.IntegerField(db_column='numMaxExtrasEnLista')  # Field name made lowercase.
    esdatosreservapais = models.IntegerField(db_column='esDatosReservaPais')  # Field name made lowercase.
    esdatosreservadireccion = models.IntegerField(db_column='esDatosReservaDireccion')  # Field name made lowercase.
    esmoduloagentes = models.IntegerField(db_column='esModuloAgentes', blank=True,
                                          null=True)  # Field name made lowercase.
    escabecerapiepersonalizado = models.IntegerField(
        db_column='esCabeceraPiePersonalizado')  # Field name made lowercase.
    esbloqueoextras = models.IntegerField(db_column='esBloqueoExtras')  # Field name made lowercase.
    limiteavisodisponibilidad = models.IntegerField(db_column='limiteAvisoDisponibilidad')  # Field name made lowercase.
    emailavisodispo = models.CharField(db_column='emailAvisoDispo', max_length=255,
                                       blank=True)  # Field name made lowercase.
    emailremitentesobreescrito = models.CharField(db_column='emailRemitenteSobreescrito', max_length=255,
                                                  blank=True)  # Field name made lowercase.
    estextopromociones = models.IntegerField(db_column='esTextoPromociones')  # Field name made lowercase.
    esenviaremailhotel = models.IntegerField(db_column='esEnviarEmailHotel', blank=True,
                                             null=True)  # Field name made lowercase.
    ispromoscierrespordia = models.IntegerField(db_column='isPromosCierresPorDia')  # Field name made lowercase.
    esnuevogoogleanalytics = models.IntegerField(db_column='esNuevoGoogleAnalytics')  # Field name made lowercase.
    esalturalogo = models.IntegerField(db_column='esAlturaLogo')  # Field name made lowercase.
    alturacabecera = models.IntegerField(db_column='alturaCabecera')  # Field name made lowercase.
    es_encuesta_postestancia = models.IntegerField()
    es_activa_encuesta_postestancia = models.IntegerField()
    dias_encuesta_postestancia = models.IntegerField()
    dias_encuesta_preestancia = models.IntegerField(blank=True, null=True)
    es_orden_alojamientos_manual = models.IntegerField()
    es_ficha_cal_mostrar_tarifas = models.IntegerField()
    es_ws_consume_reserva = models.IntegerField()
    es_importe_adelantado_oculto = models.IntegerField()
    es_promo_mostrar_prcj_ficha = models.IntegerField()
    es_ws_infotc = models.IntegerField()
    es_ws_infohotel = models.IntegerField()
    es_ws_infomoneda = models.IntegerField()
    es_email_intro_cierre = models.IntegerField()
    es_version_6 = models.IntegerField()
    es_version6_activa = models.IntegerField()
    es_filtros_blanco = models.IntegerField()
    es_filtros_menorigual = models.IntegerField()
    es_conv_divisas_oculto = models.IntegerField()
    es_alterar_orden_estab_ciudad = models.IntegerField()
    es_cancelar_reserva_usuario = models.IntegerField()
    release_cancelacion_cliente = models.IntegerField()
    es_codigo_activacion_alojamientos = models.IntegerField()
    es_incremento_iva_automatico = models.IntegerField()
    es_codigo_promocional_miniform = models.IntegerField()
    es_miniform_misma_pestanya = models.IntegerField()
    divisa_defecto_activa = models.CharField(max_length=3, blank=True)
    es_mostrar_info_impuestos_step1 = models.IntegerField()
    es_ficha_ampliada_portal = models.IntegerField()
    es_facebook_520px = models.IntegerField()
    es_facebook_700 = models.IntegerField()
    es_aviso_iva_leido = models.IntegerField()
    es_aviso_iva_decision = models.IntegerField()
    idioma_backoffice = models.CharField(max_length=3)
    es_estadisticas_avanzadas = models.IntegerField()
    es_estadisticas_agente = models.IntegerField()
    num_vista_listado = models.IntegerField()
    reserva_cancelar_release = models.IntegerField()
    esdatosreservadni = models.IntegerField(db_column='esDatosReservaDni')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configurations'


class Consultas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ip = models.CharField(max_length=45, blank=True)
    datein = models.DateField(blank=True, null=True)
    dateout = models.DateField(blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    proom = models.IntegerField(blank=True, null=True)
    adultos = models.IntegerField()
    ninos = models.IntegerField()
    bebes = models.IntegerField()
    tiposhab_id = models.IntegerField(blank=True, null=True)
    query = models.CharField(max_length=255, blank=True)
    lang = models.CharField(max_length=45, blank=True)
    tid = models.CharField(max_length=64, blank=True)
    timestamp = models.DateTimeField()
    esnodisp = models.IntegerField(db_column='esNoDisp')  # Field name made lowercase.
    ischain = models.IntegerField(db_column='isChain', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultas'


class Consultasguardadas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    query = models.TextField(blank=True)
    orderby = models.CharField(db_column='orderBy', max_length=250, blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'consultasguardadas'


class Detallesreservas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idreserva = models.IntegerField()
    tipo = models.IntegerField()
    name = models.CharField(max_length=80, blank=True)
    codigo = models.IntegerField(blank=True, null=True)
    amount = models.IntegerField(blank=True, null=True)
    computedprice = models.IntegerField(blank=True, null=True)
    foreign_key = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'detallesreservas'


class Documentos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(unique=True, max_length=25)
    name = models.CharField(max_length=255, blank=True)
    tipo = models.CharField(max_length=200)
    color = models.CharField(max_length=6, blank=True)
    texto = models.TextField(blank=True)
    html = models.TextField(blank=True)
    html_entrada = models.TextField(blank=True)
    html_salida = models.TextField(blank=True)
    html_cancelaciones = models.TextField(blank=True)
    html_cond_ninos = models.TextField(blank=True)
    html_mascotas = models.TextField(blank=True)
    html_grupos = models.TextField(blank=True)
    html_info_adicional = models.TextField(blank=True)
    orden = models.IntegerField()
    fechaini = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    vartarifas = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    cobroanticipado = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    importeminimo = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    escobrarprimeranoche = models.IntegerField(db_column='esCobrarPrimeraNoche')  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documentos'


class Documentospromociones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    documento = models.ForeignKey(Documentos, blank=True, null=True)
    promocion = models.ForeignKey('Promociones', blank=True, null=True)
    creacion = models.DateTimeField(blank=True, null=True)
    modificacion = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'documentospromociones'


class Documentossistemaspagos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    documento = models.ForeignKey(Documentos)
    sistemapago = models.ForeignKey('Sistemaspago')
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'documentossistemaspagos'


class Editorespeciales(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.CharField(max_length=90)
    id_ext = models.IntegerField()
    orden = models.IntegerField()
    name = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'editorespeciales'


class Emailconfiguraciones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    servidor = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    puerto = models.IntegerField()
    tipo = models.CharField(unique=True, max_length=255)
    prioridad = models.IntegerField()
    creado = models.DateTimeField()
    modificado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'emailconfiguraciones'


class Emails(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    idreservamultiple = models.CharField(max_length=15, blank=True)
    remitente = models.CharField(max_length=255)
    nombreremitente = models.CharField(max_length=255)
    destinatario = models.CharField(max_length=255)
    asunto = models.CharField(max_length=255)
    cuerpohtml = models.TextField()
    cuerpotexto = models.TextField()
    procesado = models.DateTimeField(blank=True, null=True)
    ultimamodif = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'emails'


class Encuestas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    titulo = models.CharField(max_length=255)
    contenido = models.TextField(blank=True)
    texto_confirmacion = models.TextField(blank=True)
    texto_cabecera_web = models.TextField(blank=True)
    texto_pie_web = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'encuestas'


class EncuestasPreguntas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pregunta = models.CharField(max_length=255, blank=True)
    seleccionada = models.IntegerField()
    es_comentario_obligatorio = models.IntegerField()
    encuesta = models.ForeignKey(Encuestas, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'encuestas_preguntas'


class EncuestasRespuestas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField()
    pregunta = models.ForeignKey(EncuestasPreguntas)
    reserva = models.ForeignKey('Reservas')
    puntuacion = models.FloatField()
    comentario = models.CharField(max_length=255, blank=True)
    confirmado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'encuestas_respuestas'


class Establecimientos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(max_length=155, blank=True)
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=2000, blank=True)
    ciudad = models.CharField(max_length=200, blank=True)
    zona = models.CharField(max_length=255, blank=True)
    pais = models.CharField(max_length=200, blank=True)
    latitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    longitud = models.DecimalField(max_digits=10, decimal_places=7, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True)
    telefono = models.CharField(max_length=20, blank=True)
    emailadmin = models.CharField(max_length=100, blank=True)
    emailsreservas = models.CharField(max_length=255, blank=True)
    orden = models.IntegerField(blank=True, null=True)
    creado = models.DateTimeField()
    modificado = models.DateTimeField(blank=True, null=True)
    visible = models.IntegerField()
    valoracion = models.IntegerField(blank=True, null=True)
    tipo = models.CharField(max_length=255, blank=True)
    es_on_request = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establecimientos'


class EstablecimientosGestores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(max_length=255)
    establecimiento_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'establecimientos_gestores'


class EstablecimientosServicios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    establecimiento_id = models.IntegerField()
    servicio_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'establecimientos_servicios'


class Establecimientosdocumentos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    establecimiento_id = models.IntegerField()
    documento_id = models.IntegerField()
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'establecimientosdocumentos'


class Extras(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255, blank=True)
    descripcion = models.TextField(blank=True)
    codigo = models.CharField(max_length=10)
    fechaini = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    xdia = models.IntegerField(blank=True, null=True)
    xpersona = models.IntegerField(blank=True, null=True)
    xreserva = models.IntegerField(blank=True, null=True)
    obligatorio = models.IntegerField()
    mindias = models.IntegerField(blank=True, null=True)
    minantelacion = models.IntegerField()
    maxantelacion = models.IntegerField(blank=True, null=True)
    anyadirpersonas = models.IntegerField()
    eleccionnumerica = models.IntegerField()
    maxeleccionnumerica = models.IntegerField()
    tipo = models.CharField(max_length=45)
    subtipo = models.CharField(max_length=45, blank=True)
    minpeople = models.IntegerField(blank=True, null=True)
    maxpeople = models.IntegerField(blank=True, null=True)
    tipohuesped = models.IntegerField()
    sensibletipohuesped = models.IntegerField()
    color = models.CharField(max_length=45, blank=True)
    activa = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()
    timestamp = models.DateTimeField()
    documento_id = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_valor = models.CharField(max_length=100)
    automatico = models.IntegerField()
    grupo = models.IntegerField()
    mensajeinformativo = models.TextField()
    tarifavariable = models.IntegerField()
    tickertarifavariable = models.CharField(max_length=15, blank=True)
    propiedades = models.TextField(blank=True)
    establecimiento_id = models.IntegerField(blank=True, null=True)
    ftarifa = models.CharField(max_length=255, blank=True)
    ftarifa_tip = models.IntegerField(blank=True, null=True)
    fbloqueo = models.CharField(max_length=255, blank=True)
    fbloqueo_tip = models.IntegerField(blank=True, null=True)
    fvariable = models.CharField(max_length=255, blank=True)
    fvariable_tip = models.IntegerField(blank=True, null=True)
    festancia_minima = models.CharField(max_length=255, blank=True)
    festancia_minima_tip = models.IntegerField(blank=True, null=True)
    festancia_maxima = models.CharField(max_length=255, blank=True)
    festancia_maxima_tip = models.IntegerField(blank=True, null=True)
    frelease_minimo = models.CharField(max_length=255, blank=True)
    frelease_minimo_tip = models.IntegerField(blank=True, null=True)
    frelease_maximo = models.CharField(max_length=255, blank=True)
    frelease_maximo_tip = models.IntegerField(blank=True, null=True)
    fvalor = models.CharField(max_length=255, blank=True)
    fbloqvalidez = models.CharField(max_length=255, blank=True)
    fstock = models.CharField(max_length=255, blank=True)
    codigopromocional = models.CharField(max_length=4092, blank=True)

    class Meta:
        managed = False
        db_table = 'extras'


class Extrasfechas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.ForeignKey('Fechas', blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    extra = models.ForeignKey(Extras, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disponibilidad = models.IntegerField(blank=True, null=True)
    cerrada = models.IntegerField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'extrasfechas'


class Extrastiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    extra = models.ForeignKey(Extras, blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    anyo = models.ForeignKey(Anyos, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'extrastiposhabs'


class Extrastiposhuesped(models.Model):
    id = models.IntegerField(primary_key=True)
    extra_id = models.IntegerField()
    tiposhuesped_id = models.IntegerField()
    ultimamodificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'extrastiposhuesped'


class Fechas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'fechas'


class Formulariosreservas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    forma = models.CharField(max_length=200)
    atributoscss = models.TextField()
    idioma = models.CharField(max_length=10)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'formulariosreservas'


class Groups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'groups'


class I18N(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    locale = models.CharField(max_length=6)
    model = models.CharField(max_length=255)
    foreign_key = models.IntegerField()
    field = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    sincronizada = models.IntegerField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'i18n'


class Impuestos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tipo = models.ForeignKey('ImpuestosTipos')
    nombre = models.CharField(max_length=45)
    valor = models.DecimalField(max_digits=10, decimal_places=7)
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'impuestos'


class ImpuestosTipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=45)
    por_defecto = models.IntegerField()
    creacion = models.DateTimeField()
    modificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'impuestos_tipos'


class InstantPaymentNotifications(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    notify_version = models.CharField(max_length=64, blank=True)
    verify_sign = models.CharField(max_length=127, blank=True)
    test_ipn = models.IntegerField(blank=True, null=True)
    address_city = models.CharField(max_length=40, blank=True)
    address_country = models.CharField(max_length=64, blank=True)
    address_country_code = models.CharField(max_length=2, blank=True)
    address_name = models.CharField(max_length=128, blank=True)
    address_state = models.CharField(max_length=40, blank=True)
    address_status = models.CharField(max_length=20, blank=True)
    address_street = models.CharField(max_length=200, blank=True)
    address_zip = models.CharField(max_length=20, blank=True)
    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    payer_business_name = models.CharField(max_length=127, blank=True)
    payer_email = models.CharField(max_length=127, blank=True)
    payer_id = models.CharField(max_length=13, blank=True)
    payer_status = models.CharField(max_length=20, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)
    residence_country = models.CharField(max_length=2, blank=True)
    business = models.CharField(max_length=127, blank=True)
    item_name = models.CharField(max_length=127, blank=True)
    item_number = models.CharField(max_length=127, blank=True)
    quantity = models.CharField(max_length=127, blank=True)
    receiver_email = models.CharField(max_length=127, blank=True)
    receiver_id = models.CharField(max_length=13, blank=True)
    custom = models.CharField(max_length=255, blank=True)
    invoice = models.CharField(max_length=127, blank=True)
    memo = models.CharField(max_length=255, blank=True)
    option_name_1 = models.CharField(max_length=64, blank=True)
    option_name_2 = models.CharField(max_length=64, blank=True)
    option_selection1 = models.CharField(max_length=200, blank=True)
    option_selection2 = models.CharField(max_length=200, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    auth_id = models.CharField(max_length=19, blank=True)
    auth_exp = models.CharField(max_length=28, blank=True)
    auth_amount = models.IntegerField(blank=True, null=True)
    auth_status = models.CharField(max_length=20, blank=True)
    num_cart_items = models.IntegerField(blank=True, null=True)
    parent_txn_id = models.CharField(max_length=19, blank=True)
    payment_date = models.CharField(max_length=28, blank=True)
    payment_status = models.CharField(max_length=20, blank=True)
    payment_type = models.CharField(max_length=10, blank=True)
    pending_reason = models.CharField(max_length=20, blank=True)
    reason_code = models.CharField(max_length=20, blank=True)
    remaining_settle = models.IntegerField(blank=True, null=True)
    shipping_method = models.CharField(max_length=64, blank=True)
    shipping = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    transaction_entity = models.CharField(max_length=20, blank=True)
    txn_id = models.CharField(max_length=19, blank=True)
    txn_type = models.CharField(max_length=20, blank=True)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_currency = models.CharField(max_length=3, blank=True)
    mc_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_gross = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_handling = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_shipping = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_gross = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    settle_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    settle_currency = models.CharField(max_length=3, blank=True)
    auction_buyer_id = models.CharField(max_length=64, blank=True)
    auction_closing_date = models.CharField(max_length=28, blank=True)
    auction_multi_item = models.IntegerField(blank=True, null=True)
    for_auction = models.CharField(max_length=10, blank=True)
    subscr_date = models.CharField(max_length=28, blank=True)
    subscr_effective = models.CharField(max_length=28, blank=True)
    period1 = models.CharField(max_length=10, blank=True)
    period2 = models.CharField(max_length=10, blank=True)
    period3 = models.CharField(max_length=10, blank=True)
    amount1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_amount1 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_amount2 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    mc_amount3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    recurring = models.CharField(max_length=1, blank=True)
    reattempt = models.CharField(max_length=1, blank=True)
    retry_at = models.CharField(max_length=28, blank=True)
    recur_times = models.IntegerField(blank=True, null=True)
    username = models.CharField(max_length=64, blank=True)
    password = models.CharField(max_length=24, blank=True)
    subscr_id = models.CharField(max_length=19, blank=True)
    case_id = models.CharField(max_length=28, blank=True)
    case_type = models.CharField(max_length=28, blank=True)
    case_creation_date = models.CharField(max_length=28, blank=True)
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'instant_payment_notifications'


class Inventario(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.ForeignKey(Fechas)
    elemento = models.ForeignKey('InventarioElementos')
    valor = models.DecimalField(max_digits=20, decimal_places=7, blank=True, null=True)
    sincronizada = models.IntegerField()
    inicializado = models.IntegerField(blank=True, null=True)
    modificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'inventario'


class InventarioElementos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    inventario_tipo = models.ForeignKey('InventarioTipos')
    ticker = models.CharField(max_length=45)
    obsoleto = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'inventario_elementos'


class InventarioTipos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'inventario_tipos'


class InventarioTiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    inventario = models.ForeignKey(Inventario)
    tiposhabs = models.ForeignKey('Tiposhabs')

    class Meta:
        managed = False
        db_table = 'inventario_tiposhabs'


class L10Ncatalogs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    code = models.CharField(max_length=45, blank=True)
    locale = models.CharField(max_length=45, blank=True)
    localefallback = models.CharField(db_column='localeFallback', max_length=45,
                                      blank=True)  # Field name made lowercase.
    charset = models.CharField(max_length=45, blank=True)
    active = models.IntegerField()
    soportado = models.IntegerField()
    visible = models.IntegerField()
    translated = models.IntegerField()
    redirected = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'l10ncatalogs'


class L10NcatalogsFull(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    code = models.CharField(max_length=45, blank=True)
    locale = models.CharField(max_length=45, blank=True)
    localefallback = models.CharField(db_column='localeFallback', max_length=45,
                                      blank=True)  # Field name made lowercase.
    charset = models.CharField(max_length=45, blank=True)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'l10ncatalogs_full'


class L10Nmaps(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    iso639_3 = models.CharField(max_length=45, blank=True)
    l10n = models.CharField(max_length=45, blank=True)
    active = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'l10nmaps'


class Mensajes(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=90)
    editedname = models.CharField(max_length=90)
    visible = models.IntegerField(blank=True, null=True)
    seccion = models.CharField(max_length=100, blank=True)
    tipo = models.CharField(max_length=7)
    titulo = models.CharField(max_length=100, blank=True)
    descripcion = models.TextField(blank=True)
    fcreacion = models.DateTimeField(blank=True, null=True)
    fmodificacion = models.DateTimeField(blank=True, null=True)
    fechainicio = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    finireserva = models.DateField(blank=True, null=True)
    ffinreserva = models.DateField(blank=True, null=True)
    alojamientos = models.CharField(max_length=8192, blank=True)

    class Meta:
        managed = False
        db_table = 'mensajes'


class Meses(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)

    class Meta:
        managed = False
        db_table = 'meses'


class Multimedia(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255, blank=True)
    entity = models.CharField(max_length=50)
    id_entity = models.IntegerField()
    file = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'multimedia'


class Newsletter(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    email = models.CharField(unique=True, max_length=100)
    language = models.CharField(max_length=3)
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'newsletter'


class Nodisponibles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ip = models.CharField(max_length=45, blank=True)
    datein = models.DateField(blank=True, null=True)
    dateout = models.DateField(blank=True, null=True)
    nights = models.IntegerField(blank=True, null=True)
    rooms = models.IntegerField(blank=True, null=True)
    proom = models.IntegerField(blank=True, null=True)
    tiposhab_id = models.IntegerField(blank=True, null=True)
    query = models.CharField(max_length=255, blank=True)
    lang = models.CharField(max_length=45, blank=True)
    tid = models.CharField(max_length=64, blank=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'nodisponibles'


class Packs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    codigo = models.CharField(max_length=45, blank=True)
    descripcion = models.TextField(blank=True)
    fechainicontrat = models.DateField(blank=True, null=True)
    fechafincontrat = models.DateField()
    fechainiactivo = models.DateField(blank=True, null=True)
    fechafinactivo = models.DateField(blank=True, null=True)
    precioxdia = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    precioxreserva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    xdia = models.IntegerField(blank=True, null=True)
    xpersona = models.IntegerField(blank=True, null=True)
    xreserva = models.IntegerField(blank=True, null=True)
    numpersonas = models.IntegerField()
    mindias = models.IntegerField(blank=True, null=True)
    maxdias = models.IntegerField()
    tipo = models.CharField(max_length=45)
    activa = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField()
    timestamp = models.DateTimeField()
    documento_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=45, blank=True)
    tipo_valor = models.CharField(max_length=100)
    maxeleccionnumerica = models.IntegerField()
    versiones = models.TextField()

    class Meta:
        managed = False
        db_table = 'packs'


class Packsfechas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.ForeignKey(Fechas, blank=True, null=True)
    tiposhab = models.ForeignKey('Packstiposhabs', blank=True, null=True)
    pack = models.ForeignKey(Packs, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disponibilidad = models.IntegerField(blank=True, null=True)
    cerrada = models.IntegerField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'packsfechas'


class Packstiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    pack = models.ForeignKey(Packs, blank=True, null=True)
    tipohab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    anyo = models.ForeignKey(Anyos, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'packstiposhabs'


class Pages(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(unique=True, max_length=25)
    title = models.CharField(max_length=15)
    description = models.TextField(blank=True)
    seo = models.TextField(blank=True)
    parent = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pages'


class Paises(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255)
    alfa2 = models.CharField(max_length=2)
    alfa3 = models.CharField(max_length=3)
    codigo = models.CharField(max_length=3)
    iso3661_2 = models.CharField(max_length=14)

    class Meta:
        managed = False
        db_table = 'paises'


class Perfilescolor(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=200)
    colorlinia = models.CharField(db_column='colorLinia', max_length=10, blank=True)  # Field name made lowercase.
    botonminiform = models.CharField(db_column='botonMiniForm', max_length=10, blank=True)  # Field name made lowercase.
    fondocabecera = models.CharField(db_column='fondoCabecera', max_length=10, blank=True)  # Field name made lowercase.
    colorcabecera = models.CharField(db_column='colorCabecera', max_length=10, blank=True)  # Field name made lowercase.
    colorcabecerainactivo = models.CharField(db_column='colorCabeceraInactivo', max_length=10,
                                             blank=True)  # Field name made lowercase.
    fondopasos = models.CharField(db_column='fondoPasos', max_length=10, blank=True)  # Field name made lowercase.
    colorpasos = models.CharField(db_column='colorPasos', max_length=10, blank=True)  # Field name made lowercase.
    fondocuerpo = models.CharField(db_column='fondoCuerpo', max_length=10, blank=True)  # Field name made lowercase.
    colorcuerpo = models.CharField(db_column='colorCuerpo', max_length=10, blank=True)  # Field name made lowercase.
    colorcuerpoinactivo = models.CharField(db_column='colorCuerpoInactivo', max_length=10,
                                           blank=True)  # Field name made lowercase.
    colorbotonescuerpo = models.CharField(db_column='colorBotonesCuerpo', max_length=10,
                                          blank=True)  # Field name made lowercase.
    fondobotonescuerpo = models.CharField(db_column='fondoBotonesCuerpo', max_length=10,
                                          blank=True)  # Field name made lowercase.
    alturacabecera = models.IntegerField(db_column='alturaCabecera')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'perfilescolor'


class Promociones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    codigo = models.CharField(max_length=45, blank=True)
    descripcion = models.TextField(blank=True)
    fechaini = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    porcentaje = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    textoexplicativo = models.CharField(db_column='textoExplicativo', max_length=5,
                                        blank=True)  # Field name made lowercase.
    xdia = models.IntegerField(blank=True, null=True)
    xpersona = models.IntegerField(blank=True, null=True)
    xreserva = models.IntegerField(blank=True, null=True)
    mindias = models.IntegerField()
    maxdias = models.IntegerField()
    minantelacion = models.IntegerField()
    maxantelacion = models.IntegerField()
    tipo = models.CharField(max_length=45)
    activa = models.IntegerField(blank=True, null=True)
    orden = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField()
    documento_id = models.IntegerField(blank=True, null=True)
    color = models.CharField(max_length=45, blank=True)
    habitaciones = models.CharField(max_length=255)
    codigopromocional = models.CharField(max_length=4092, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    tipo_valor = models.CharField(max_length=100)
    grupo = models.IntegerField()
    automatico = models.IntegerField()
    acumulable = models.IntegerField()
    mensajeinformativo = models.TextField()
    preciomin = models.DecimalField(max_digits=10, decimal_places=4)
    preciomax = models.DecimalField(max_digits=10, decimal_places=4)
    prcjpago = models.DecimalField(max_digits=10, decimal_places=9)
    estanciaminima = models.IntegerField()
    fechainicontratacion = models.DateField(blank=True, null=True)
    fechafincontratacion = models.DateField(blank=True, null=True)
    condicionregimenes = models.CharField(max_length=255, blank=True)
    escierrevariable = models.IntegerField(db_column='esCierreVariable')  # Field name made lowercase.
    tickercierrevariable = models.CharField(db_column='tickerCierreVariable', max_length=12,
                                            blank=True)  # Field name made lowercase.
    propiedades = models.TextField(blank=True)
    establecimiento_id = models.IntegerField(blank=True, null=True)
    esincompatibleconopcionales = models.IntegerField(
        db_column='esIncompatibleConOpcionales')  # Field name made lowercase.
    ftarifa = models.CharField(max_length=255, blank=True)
    ftarifa_tip = models.IntegerField(blank=True, null=True)
    tipotarifa = models.IntegerField(blank=True, null=True)
    fbloqueo = models.CharField(max_length=255, blank=True)
    fbloqueo_tip = models.IntegerField(blank=True, null=True)
    fvariable = models.CharField(max_length=255, blank=True)
    fvariable_tip = models.IntegerField(blank=True, null=True)
    festancia_minima = models.CharField(max_length=255, blank=True)
    festancia_minima_tip = models.IntegerField(blank=True, null=True)
    festancia_maxima = models.CharField(max_length=255, blank=True)
    festancia_maxima_tip = models.IntegerField(blank=True, null=True)
    frelease_minimo = models.CharField(max_length=255, blank=True)
    frelease_minimo_tip = models.IntegerField(blank=True, null=True)
    frelease_maximo = models.CharField(max_length=255, blank=True)
    frelease_maximo_tip = models.IntegerField(blank=True, null=True)
    fvalor = models.CharField(max_length=255, blank=True)
    fbloqvalidez = models.CharField(max_length=255, blank=True)
    fstock = models.CharField(max_length=255, blank=True)
    es_no_cancelable = models.IntegerField()
    automatica = models.IntegerField()
    num_noches_promo = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promociones'


class Promocionesfechas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.ForeignKey(Fechas, blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    promocione = models.ForeignKey(Promociones, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    disponibilidad = models.IntegerField(blank=True, null=True)
    cerrada = models.IntegerField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promocionesfechas'


class Promocionestiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    promocione = models.ForeignKey(Promociones, blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    anyo = models.ForeignKey(Anyos, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'promocionestiposhabs'


class Propietariostiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey('Users')
    tiposhab = models.ForeignKey('Tiposhabs')

    class Meta:
        managed = False
        db_table = 'propietariostiposhabs'


class Requests(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    consulta = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'requests'


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
    tiposhabs = models.ForeignKey('Tiposhabs', blank=True, null=True)
    tid = models.CharField(max_length=64, blank=True)
    idafiliado = models.CharField(max_length=1024, blank=True)
    idafiliadoreducido = models.CharField(max_length=255, blank=True)
    importepago = models.DecimalField(max_digits=20, decimal_places=4)
    prcjpago = models.DecimalField(max_digits=12, decimal_places=7)
    depositofijo = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    sistemapago_id = models.IntegerField(blank=True, null=True)
    ip = models.CharField(max_length=255, blank=True)
    googleanalyticsok = models.IntegerField(blank=True, null=True)
    idioma = models.CharField(max_length=3, blank=True)
    pais = models.CharField(max_length=255, blank=True)
    ultimamodificacion = models.DateTimeField(blank=True, null=True)
    agente_id = models.IntegerField(blank=True, null=True)
    motivocancelacion = models.TextField(blank=True)
    f_cancelacion = models.DateTimeField(blank=True, null=True)
    emailing = models.IntegerField(blank=True, null=True)
    fenvio_pre_stay = models.DateField(blank=True, null=True)
    fenvio_encuesta_post_estancia = models.DateField(blank=True, null=True)
    es_consultada_ws = models.IntegerField()
    es_solicita_cancelacion = models.IntegerField()
    control_confirmadas = models.CharField(max_length=255, blank=True)
    prcj_impuestos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_promos_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    prcj_promos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_aloj_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    codigo_aplicado = models.CharField(max_length=255, blank=True)
    tracking_trivago = models.CharField(max_length=255, blank=True)
    commission = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    reserva_cancelar_release = models.IntegerField()
    dni = models.CharField(max_length=50, blank=True)
    referer = models.CharField(max_length=1024, blank=True)
    userreservationemailstatus = models.CharField(db_column='userReservationEmailStatus', max_length=64,
                                                  blank=True)  # Field name made lowercase.
    hotelreservationemailstatus = models.CharField(db_column='hotelReservationEmailStatus', max_length=64,
                                                   blank=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'reservas'


class Reservasborradas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fechaentrada = models.DateField()
    fechasalida = models.DateField()
    nombre = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    estado = models.CharField(max_length=10)
    estadoampliado = models.IntegerField()
    habitaciones = models.IntegerField()
    noches = models.IntegerField()
    capacidad = models.IntegerField()
    bebes = models.IntegerField(blank=True, null=True)
    importe = models.DecimalField(max_digits=20, decimal_places=4)
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
    tiposhabs = models.ForeignKey('Tiposhabs', blank=True, null=True)
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
    ultimamodificacion = models.DateTimeField(blank=True, null=True)
    agente_id = models.IntegerField(blank=True, null=True)
    motivocancelacion = models.TextField(blank=True)
    f_cancelacion = models.DateTimeField(blank=True, null=True)
    emailing = models.IntegerField(blank=True, null=True)
    fenvio_encuesta_post_estancia = models.DateField(blank=True, null=True)
    es_consultada_ws = models.IntegerField()
    es_solicita_cancelacion = models.IntegerField()
    control_confirmadas = models.CharField(max_length=255, blank=True)
    prcj_impuestos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_promos_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    prcj_promos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_aloj_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    codigo_aplicado = models.CharField(max_length=255, blank=True)
    tracking_trivago = models.CharField(max_length=255, blank=True)
    reserva_cancelar_release = models.IntegerField()
    dni = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'reservasborradas'


class Reservasdetalles(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    reserva = models.ForeignKey(Reservas)
    clave = models.CharField(max_length=15)
    valor = models.CharField(max_length=8912)
    ultimamodif = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'reservasdetalles'


class Reservasmodificadas(models.Model):
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
    ultimamodificacion = models.DateTimeField(blank=True, null=True)
    agente_id = models.IntegerField(blank=True, null=True)
    motivocancelacion = models.TextField(blank=True)
    f_cancelacion = models.DateTimeField(blank=True, null=True)
    emailing = models.IntegerField(blank=True, null=True)
    fenvio_encuesta_post_estancia = models.DateField(blank=True, null=True)
    es_consultada_ws = models.IntegerField()
    es_solicita_cancelacion = models.IntegerField()
    control_confirmadas = models.CharField(max_length=255, blank=True)
    prcj_impuestos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_promos_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    prcj_promos = models.DecimalField(max_digits=12, decimal_places=7, blank=True, null=True)
    importe_aloj_sin_impuestos = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    codigo_aplicado = models.CharField(max_length=255, blank=True)
    tracking_trivago = models.CharField(max_length=255, blank=True)
    reserva_cancelar_release = models.IntegerField()
    dni = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'reservasmodificadas'


class Scripts(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=255)
    code = models.TextField(blank=True)
    position = models.CharField(max_length=255, blank=True)
    place = models.CharField(max_length=255, blank=True)
    onetime = models.IntegerField(db_column='oneTime')  # Field name made lowercase.
    active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'scripts'


class Servicios(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    nombre = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'servicios'


class Sistemapagoconexiones(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    sistemapago = models.ForeignKey('Sistemaspago')
    propiedad = models.CharField(unique=True, max_length=255)
    variable = models.CharField(max_length=255, blank=True)
    valor = models.CharField(max_length=255)
    creado = models.DateTimeField(blank=True, null=True)
    modificado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sistemapagoconexiones'


class Sistemaspago(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    ticker = models.CharField(max_length=12, blank=True)
    nombre = models.CharField(max_length=255)
    textodescriptivo = models.TextField(blank=True)
    prcjpago = models.DecimalField(max_digits=8, decimal_places=4)
    escobroanticipado = models.IntegerField()
    activo = models.IntegerField()
    creado = models.DateTimeField()
    modificado = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'sistemaspago'


class Tarifas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=45, blank=True)
    orden = models.IntegerField()
    color = models.CharField(max_length=10)
    anyo = models.ForeignKey(Anyos)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tarifas'


class Tarifasfechas(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    fecha = models.ForeignKey(Fechas, blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    precio = models.DecimalField(max_digits=17, decimal_places=6, blank=True, null=True)
    disponibilidad = models.IntegerField(blank=True, null=True)
    estanciaminima = models.IntegerField()
    cerrada = models.IntegerField()
    marca = models.IntegerField()
    sincronizada = models.IntegerField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tarifasfechas'


class Tarifastiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    tarifa = models.ForeignKey(Tarifas, blank=True, null=True)
    tiposhab = models.ForeignKey('Tiposhabs', blank=True, null=True)
    anyo = models.ForeignKey(Anyos, blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=3)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tarifastiposhabs'


class Tarjetascredito(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    codigo = models.CharField(max_length=255, blank=True)
    nombre = models.CharField(max_length=255, blank=True)
    activa = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tarjetascredito'


class Tiposhabs(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    formula_antigua_test = models.CharField(max_length=255)
    alojamientotipo = models.ForeignKey(AlojamientoTipos, blank=True, null=True)
    alojamientoconfiguracion = models.ForeignKey(AlojamientoConfiguraciones, blank=True, null=True)
    complemento = models.ForeignKey(Complementos, blank=True, null=True)
    condiciones = models.ForeignKey(Documentos, blank=True, null=True)
    impuesto = models.ForeignKey(Impuestos, blank=True, null=True)
    establecimiento_id = models.IntegerField(blank=True, null=True)
    codigo = models.CharField(unique=True, max_length=45, blank=True)
    name = models.CharField(max_length=45, blank=True)
    tipo = models.CharField(max_length=25, blank=True)
    tipotxt = models.CharField(max_length=255, blank=True)
    capacidad = models.IntegerField()
    adultos = models.IntegerField()
    ninos = models.IntegerField()
    bebes = models.IntegerField()
    esadmitebebes = models.IntegerField()
    formulabebes = models.CharField(max_length=255, blank=True)
    cancelable = models.IntegerField()
    stock = models.IntegerField()
    info = models.TextField(blank=True)
    infoorig = models.TextField(blank=True)
    order = models.IntegerField()
    orden_manual = models.IntegerField()
    images = models.TextField()
    activa = models.IntegerField()
    autoaddextras = models.CharField(max_length=255)
    lastmodified = models.DateTimeField()
    codigobookingbooster = models.CharField(max_length=50)
    tipoelemento = models.CharField(max_length=1)
    versionspack = models.TextField()
    propiedades = models.TextField()
    capacidadmaxima = models.IntegerField()
    precioadultoextra = models.DecimalField(max_digits=10, decimal_places=3)
    precioninoextra = models.DecimalField(max_digits=10, decimal_places=3)
    items = models.TextField()
    heredaficha = models.IntegerField(blank=True, null=True)
    heredastock = models.IntegerField()
    estarifasindependientes = models.IntegerField()
    escierresindependientes = models.IntegerField()
    esestminindependientes = models.IntegerField(db_column='esEstMinIndependientes')  # Field name made lowercase.
    condicionesreserva = models.TextField(blank=True)
    vartarifaporcentaje = models.DecimalField(max_digits=6, decimal_places=3)
    vartarifafijo = models.DecimalField(max_digits=6, decimal_places=3)
    subtipo = models.CharField(max_length=3)
    mindias = models.IntegerField(blank=True, null=True)
    maxdias = models.IntegerField(blank=True, null=True)
    fechaini = models.DateField(blank=True, null=True)
    fechafin = models.DateField(blank=True, null=True)
    minantelacion = models.IntegerField(blank=True, null=True)
    maxantelacion = models.IntegerField(blank=True, null=True)
    formula = models.CharField(max_length=255, blank=True)
    formula_tarifa = models.CharField(max_length=255, blank=True)
    es_formula_tarifa = models.IntegerField()
    ftarifa = models.CharField(max_length=255, blank=True)
    ftarifa_tip = models.IntegerField(blank=True, null=True)
    fdisponibilidad = models.CharField(max_length=75, blank=True)
    fdisponibilidad_tip = models.IntegerField(blank=True, null=True)
    festancia_minima = models.CharField(max_length=75, blank=True)
    festancia_minima_tip = models.IntegerField(blank=True, null=True)
    festancia_maxima = models.CharField(max_length=75, blank=True)
    festancia_maxima_tip = models.IntegerField(blank=True, null=True)
    frelease_minimo = models.CharField(max_length=75, blank=True)
    frelease_minimo_tip = models.IntegerField(blank=True, null=True)
    frelease_maximo = models.CharField(max_length=75, blank=True)
    frelease_maximo_tip = models.IntegerField(blank=True, null=True)
    fbloqueo = models.CharField(max_length=75, blank=True)
    fbloqueo_tip = models.IntegerField(blank=True, null=True)
    fcreacion = models.DateTimeField(blank=True, null=True)
    fmodificacion = models.DateTimeField(blank=True, null=True)
    codigo_acceso = models.TextField()
    dias_entrada = models.CharField(max_length=13)
    dias_salida = models.CharField(max_length=13)
    version = models.IntegerField()
    codigo_tarifa = models.CharField(max_length=384, blank=True)
    codigo_activacion = models.CharField(max_length=15, blank=True)
    es_nueva = models.IntegerField()
    es_padre_tarifa = models.IntegerField()
    migrado = models.IntegerField()
    deleted = models.IntegerField()
    rack = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tiposhabs'


class Tiposhabscomplementos(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    complemento = models.ForeignKey(Complementos)
    tiposhab = models.ForeignKey(Tiposhabs)
    formula = models.CharField(max_length=255)
    ultimamodif = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tiposhabscomplementos'


class Tiposhuesped(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    tipo = models.IntegerField()
    ultimamodificacion = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'tiposhuesped'


class Trackings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    cookie_id = models.CharField(max_length=64, blank=True)
    ip = models.CharField(max_length=20, blank=True)
    info = models.TextField(blank=True)
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'trackings'


class Users(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    username = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=40)
    group_id = models.IntegerField()
    created = models.DateTimeField(blank=True, null=True)
    modified = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'


class Witcache(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(unique=True, max_length=255)
    value1 = models.TextField()
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'witcache'


class Witcontrol(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    key = models.CharField(max_length=255)
    value = models.CharField(max_length=255)
    lastmodified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'witcontrol'


class Witportals(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    url = models.CharField(max_length=255, blank=True)
    key = models.CharField(max_length=255, blank=True)

    class Meta:
        managed = False
        db_table = 'witportals'
