from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('consultar/', views.consultar_form, name='consultar'),
    path('consultar/<str:codigo>/', views.detalle_pedido, name='detalle_pedido'),
    path('registro/', views.registro_cliente, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('panel-cliente/', views.panel_cliente, name='panel_cliente'),
    path('panel-trabajador/', views.panel_trabajador, name='panel_trabajador'),
]