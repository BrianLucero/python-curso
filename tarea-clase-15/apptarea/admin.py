from django.contrib import admin

from apptarea.models import *

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Pedido)
admin.site.register(Usuarios)
admin.site.register(Pago)
admin.site.register(TipoEnvio)
admin.site.register(UsuarioPedido)
admin.site.register(ProductoPedido)
admin.site.register(Categoria)