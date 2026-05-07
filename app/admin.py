from django.contrib import admin
from .models import Repartidor,Producto,Pedido,DetallePedido,PerfilCliente,PerfilTrabajador

# Register your models here.
admin.site.register(Repartidor)
admin.site.register(Producto)
admin.site.register(Pedido)
admin.site.register(DetallePedido)
admin.site.register(PerfilCliente)
admin.site.register(PerfilTrabajador)
