from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Pedido, DetallePedido, PerfilCliente
from .forms import RegistroClienteForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    if hasattr(request.user, 'perfilcliente'):
        return redirect('panel_cliente')
    elif hasattr(request.user, 'perfiltrabajador'):
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

def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            usuario = form.save(commit=False)
            usuario.username = f"{form.cleaned_data['first_name']}{form.cleaned_data['last_name']}"
            usuario.set_password(form.cleaned_data['password1'])
            usuario.save()
            PerfilCliente.objects.create(usuario=usuario)
            return redirect('consultar')
    else:
        form = RegistroClienteForm()
    return render(request, 'app/registro_cliente.html', {'form': form})

@login_required
def panel_cliente(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, 'app/panel_cliente.html', {'pedidos': pedidos})

@login_required
def panel_trabajador(request):
    pedidos = Pedido.objects.all().order_by('-fecha')
    return render(request, 'app/panel_trabajador.html', {'pedidos': pedidos})