from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarMensajesView.as_view(), name='listar_mensajes'),
    path('crear/', views.CrearMensajeView.as_view(), name='crear_mensaje'),
    path('eliminar/<int:pk>/', views.EliminarMensajeView.as_view(), name='eliminar_mensaje'),
    path('seleccionar_usuario/', views.SeleccionarUsuarioView.as_view(), name='seleccionar_usuario'),
]
