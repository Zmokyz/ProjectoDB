from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Pedido, DetallePedido
from .forms import EditarPedidoForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    if hasattr(request.user, 'perfiltrabajador'):
        return redirect('panel_trabajador')
    else:
        return render(request, 'app/home.html')

def consultar_form(request):
    if request.method == 'POST':
        codigo = request.POST.get('codigo_pedido')
        return redirect('detalle_pedido', codigo=codigo)
    return render(request, 'app/consultar.html')

def detalle_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo_pedido=codigo)
    detalles = DetallePedido.objects.filter(pedido=pedido)
    return render(request, 'app/detalle_pedido.html', {
        'pedido': pedido,
        'detalles': detalles,
    })  

@login_required
def panel_trabajador(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, 'app/panel_trabajador.html', {'pedidos': pedidos})

@login_required
def editar_pedido(request, codigo):
    pedido = get_object_or_404(Pedido, codigo_pedido=codigo)
    if request.method == 'POST':
        form = EditarPedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            form.save()
            return redirect('panel_trabajador')
    else:
        form = EditarPedidoForm(instance=pedido)
    return render(request, 'app/editar_pedido.html', {
        'form': form,
        'pedido': pedido,
    })
