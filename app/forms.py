from django import forms
from .models import Pedido

class EditarPedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['estado', 'repartidor']
        labels = {
            'estado': 'Estado del pedido',
            'repartidor': 'Repartidor asignado',
        }