from django.contrib import admin
import nested_admin 
from .models import Periodo, Oracao, ComponenteSintatico

# Define a visualização aninhada (inline) dos Componentes
class ComponenteSintaticoInline(nested_admin.NestedTabularInline):
    model = ComponenteSintatico
    extra = 1  # Quantos formulários em branco mostrar
    fk_name = 'oracao' 

# Define a visualização aninhada (inline) das Orações
class OracaoInline(nested_admin.NestedStackedInline):
    model = Oracao
    extra = 1
    fk_name = 'periodo'
    
    # Aninha os componentes dentro das orações
    inlines = [ComponenteSintaticoInline]

# Registra o modelo 'Periodo' principal no admin
@admin.register(Periodo)
class PeriodoAdmin(nested_admin.NestedModelAdmin):
    list_display = ('id', 'texto_completo')
    
    # Aninha as orações dentro do período
    inlines = [OracaoInline]