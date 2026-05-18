from django.db import models
from django.contrib.auth.models import User

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    direccion = models.CharField(max_length=200, blank=True)
    telefono = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Repartidor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    disponible = models.BooleanField(default=True)

    def __str__(self):
        return f"Repartidor :{self.nombre} {self.apellido}"
    
    class Meta:
        verbose_name = "Repartidor"
        verbose_name_plural = "Repartidores"


class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField(default=0)

    def __str__(self):
        return f"Producto :{self.nombre} Stock: {self.stock}"

class Pedido(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    repartidor = models.ForeignKey(Repartidor, on_delete=models.SET_NULL,
                                   null=True, blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=ESTADOS,
                              default='pendiente')
    codigo_pedido = models.CharField(max_length=30, unique=True, blank=True)

    def __str__(self):
        return self.codigo_pedido


class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.pedido.codigo_pedido}"
    

class PerfilTrabajador(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    numero_empleado = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"Trabajador: {self.usuario.username} - {self.numero_empleado}"
    
    class Meta:
        verbose_name = "Perfil de Trabajador"
        verbose_name_plural = "Perfiles de Trabajadores"