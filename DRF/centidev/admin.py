from django.contrib import admin
from . import models


@admin.register(models.Post)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('co_modulo', 'nb_opcion', 'co_tabla', 'co_estatus', 'fe_update')
    prepopulated_fields = {'slug': ('title',), }


admin.site.register(models.Category)
