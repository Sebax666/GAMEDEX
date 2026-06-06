from django.contrib import admin
from .models import Producto, Perfil


admin.site.register(Perfil)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'publicado', 'destacado')
    list_editable = ('destacado',)