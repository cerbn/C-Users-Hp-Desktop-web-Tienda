from django.contrib import admin
from .models import *


# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen']
    
class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen']





admin.site.register(TipoProducto)
admin.site.register(Producto,ProductosAdmin)
