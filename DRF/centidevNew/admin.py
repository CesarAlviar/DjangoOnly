from django.contrib import admin
from . import models


@admin.register(models.Report)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('co_modulo', 'nb_opcion', 'co_tabla', 'co_estatus', 'fe_update')

