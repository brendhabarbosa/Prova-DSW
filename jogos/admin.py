from django.contrib import admin
from jogos.models import Modalidade, Atleta, Tecnico, Equipe
# Register your models here.

@admin.register(Atleta)
class AtletaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula']
    list_filter = [ 'modalidade']
    search_fields = ['nome']

class TecnicoInline(admin.TabularInline):
    model = Tecnico
    extra = 1

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso']
    in_line = [TecnicoInline]

admin.site.register(Modalidade)
admin.site.register(Tecnico)

