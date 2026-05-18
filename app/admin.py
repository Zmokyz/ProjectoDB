from django.contrib import admin
from .models import Repartidor, Producto, Pedido, DetallePedido, Cliente, PerfilTrabajador

class DetallePedidoInline(admin.TabularInline):
    model = DetallePedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]

admin.site.register(Cliente)
admin.site.register(Repartidor)
admin.site.register(Producto)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido)
admin.site.register(PerfilTrabajador)