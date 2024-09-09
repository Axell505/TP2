from django.urls import path
from .views import MensajeCreateView, MensajesRecibidosListView, MensajesEnviadosListView, MensajeDeleteView

app_name = 'mensajes'

urlpatterns = [
    path('crear/', MensajeCreateView.as_view(), name='crear_mensaje'),
    path('recibidos/', MensajesRecibidosListView.as_view(), name='ver_recibidos'),
    path('enviados/', MensajesEnviadosListView.as_view(), name='ver_enviados'),
    path('eliminar/<int:pk>/', MensajeDeleteView.as_view(), name='eliminar_mensaje'),
]
