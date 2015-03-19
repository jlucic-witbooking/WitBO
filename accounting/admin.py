from django.contrib import admin

from accounting.models import *


class ServiceAdmin(admin.ModelAdmin):
    pass


class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('aplicacion', 'identificador', 'alta')


class ContractAdmin(admin.ModelAdmin):
    pass


class ClientAdmin(admin.ModelAdmin):
    pass


class PartnersAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ticker')


admin.site.register(Client, ClientAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(Partners, PartnersAdmin)
