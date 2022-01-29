from django.contrib import admin

# Register your models here.
from .models import LineaInvestigacion, Archivo, Integrante, Producto, Categoria, Permiso


admin.site.register(LineaInvestigacion)
admin.site.register(Archivo)
admin.site.register(Integrante)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Permiso)
