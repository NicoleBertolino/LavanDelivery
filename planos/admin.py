from django.contrib import admin

from .models import PacoteRepublica, Plano


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ("nome", "kg_mes", "preco", "coletas_semana", "prazo", "destaque")
    list_editable = ("destaque",)


@admin.register(PacoteRepublica)
class PacoteRepublicaAdmin(admin.ModelAdmin):
    list_display = ("pessoas", "kg_semana", "preco_morador", "ciclos", "coletas_semana", "destaque")
    list_editable = ("destaque",)
