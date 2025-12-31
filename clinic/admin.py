from django.contrib import admin
from .models import Paciente, Atendimento

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'criado_em')
    search_fields = ('nome', 'email')
    list_filter = ('criado_em',)
    

@admin.register(Atendimento)
class AtendimentoAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'profissional', 'data_atendimento', 'criado_em')
    search_fields = ('paciente__nome', 'profissional__username')
    list_filter = ('data_atendimento', 'criado_em')
