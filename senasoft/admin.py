from django.contrib import admin
from .models import Competidor

@admin.register(Competidor)
class CompetidorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'centro', 'categoria', 'fecha_registro')
    search_fields = ('nombre', 'centro', 'categoria')
