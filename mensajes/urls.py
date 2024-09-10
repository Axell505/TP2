from django.urls import path
from . import views
from .views import seleccionar_usuario

urlpatterns = [
    path('', views.ListarMensajesView.as_view(), name='listar_mensajes'),
    path('crear/', views.CrearMensajeView.as_view(), name='crear_mensaje'),
    path('eliminar/<int:pk>/', views.EliminarMensajeView.as_view(), name='eliminar_mensaje'),
    path('seleccionar_usuario/', seleccionar_usuario, name='seleccionar_usuario'),
]
