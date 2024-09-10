from django.views.generic import ListView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import Mensaje
from .forms import MensajeForm
from django.views import View

class ListarMensajesView(ListView):
    model = Mensaje
    template_name = 'listar_mensajes.html'
    context_object_name = 'mensajes_recibidos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Asumiendo que `usuario` es el usuario simulado
        usuario = self.request.session.get('usuario', 'Invitado')
        context['usuario'] = usuario

        # Filtra mensajes enviados por el usuario actual
        context['mensajes_enviados'] = Mensaje.objects.filter(remitente=usuario)
        
        # Filtra mensajes recibidos por el usuario actual
        context['mensajes_recibidos'] = Mensaje.objects.filter(destinatario=usuario)
        
        return context

class CrearMensajeView(CreateView):
    model = Mensaje
    form_class = MensajeForm
    template_name = 'crear_mensaje.html'
    success_url = reverse_lazy('listar_mensajes')

    def form_valid(self, form):
        # Asumiendo que `usuario` es el usuario simulado
        usuario = self.request.session.get('usuario', 'Invitado')
        form.instance.remitente = usuario
        return super().form_valid(form)

class EliminarMensajeView(DeleteView):
    model = Mensaje
    template_name = 'eliminar_mensaje.html'
    success_url = reverse_lazy('listar_mensajes')

def seleccionar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST.get('usuario')
        request.session['usuario'] = usuario
        return redirect('listar_mensajes')
    else:
        usuarios = ['Usuario1', 'Usuario2', 'Usuario3']  # Lista de usuarios simulados
        return render(request, 'seleccionar_usuario.html', {'usuarios': usuarios})