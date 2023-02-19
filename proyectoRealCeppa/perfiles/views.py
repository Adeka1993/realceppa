from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from .models import Perfil
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .models import Delegacion, Afijo
from .forms import AfijoForm, DelegacionForm, UsuarioForm, CesionarioForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import PerfilForm, PerfilUsuarioForm, TitularForm
from messenger.models import Message, Thread
from perros.models import Titular, Cesionario
from django.contrib import messages


from django.shortcuts import redirect



# Create your views here.
class PerfilListView(ListView):
    model = Perfil
    template_name = 'perfiles/perfil_list.html'
    paginate_by = 9

    def get_context_data(self, **kwargs):
        # Llamamos al método padre para obtener el contexto por defecto
        context = super().get_context_data(**kwargs)
        # Añadimos la lista de perfiles al contexto
        context['perfil_list'] = Perfil.objects.all()
        context['perfil'] = Perfil.objects.get(user=self.request.user)

        # Obtener mensajes no leídos
        messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
        # Obtener hilos a partir de mensajes
        threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
        # Contar hilos
        unread_messages = threads.count()

        # Añadir variables al contexto
        context['unread_messages'] = unread_messages
        context['threads'] = threads

        return context

    



class PerfilDetailView(DetailView):
    model =  Perfil
    template_name = 'perfiles/perfil_detail.html'
    context_object_name = 'miPerfil'

    def get_object(self):
        return get_object_or_404(Perfil, user__pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        
        # Llamamos al método padre para obtener el contexto por defecto
        context = super().get_context_data(**kwargs)

        current_titular = Titular.objects.filter(titular=self.object.user)
        context['current_titular'] = current_titular
        current_cesionario = Cesionario.objects.filter(cesionario=self.object.user)
        context['current_cesionario'] = current_cesionario
     
        # Añadimos la lista de perfiles al contexto
        context['perfil_list'] = Perfil.objects.all()
        context['perfil'] = Perfil.objects.get(user=self.request.user)

        # Obtener mensajes no leídos
        messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
        # Obtener hilos a partir de mensajes
        threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
        # Contar hilos
        unread_messages = threads.count()

        # Añadir variables al contexto
        context['unread_messages'] = unread_messages
        context['threads'] = threads

        return context


class PerfilUpdateView(UpdateView):
    model = Perfil
    template_name = 'perfiles/perfil_edit.html'
    context_object_name = 'miPerfil'
    pk_url_kwarg = 'pk'
    form_class = PerfilUsuarioForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['initial'] = {
            'first_name': self.object.user.first_name,
            'last_name': self.object.user.last_name,
            'email': self.object.user.email,

        }
   
        return kwargs

    def get_context_data(self, **kwargs):
        request = self.request

        context = super().get_context_data(**kwargs)
        current_titular = Titular.objects.filter(titular=self.object.user)
        context['current_titular'] = current_titular
        current_cesionario = Cesionario.objects.filter(cesionario=self.object.user)
        context['current_cesionario'] = current_cesionario

        # Añadir formularios al contexto
        context.update({
            'perfil_form': PerfilForm(**self.get_form_kwargs()),
            'usuario_form':UsuarioForm(**self.get_form_kwargs()),
            'titular_form': TitularForm(**self.get_form_kwargs()),
            'cesionario_form': CesionarioForm(**self.get_form_kwargs()),
        })
        context['perfil_list'] = Perfil.objects.all()
        context['perfil'] = Perfil.objects.get(user=self.request.user)
        messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
        threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
        unread_messages = threads.count()
        context['unread_messages'] = unread_messages
        return context

    def form_valid(self, form):

        
        if 'submit_cesionario_form' in self.request.POST:
            cesionario_form = CesionarioForm(self.request.POST)
            if cesionario_form.is_valid():
                if cesionario_form.cleaned_data['cesionario'] and cesionario_form.cleaned_data['perro_cesionario']:
                    # Guardar el formulario cesionario_form
                    cesionario_form.save()
                    messages.success(self.request, 'Cesión - Se ha guardado correctamente')
                    return redirect('perfiles:edit', pk=self.object.pk)
                else:
                    if not cesionario_form.cleaned_data['cesionario'] and not cesionario_form.cleaned_data['perro_cesionario']:
                        messages.error(self.request, 'Cesión - Debe seleccionar un cesionario y un ejemplar')
                        return redirect('perfiles:edit', pk=self.object.pk)
                    elif not cesionario_form.cleaned_data['cesionario']:                        
                        messages.error(self.request, 'Cesión - Debe seleccionar un cesionario')
                        return redirect('perfiles:edit', pk=self.object.pk)
                    elif not cesionario_form.cleaned_data['perro_cesionario']:
                        messages.error(self.request, 'Cesión - Debe seleccionar un ejemplar')
                        return redirect('perfiles:edit', pk=self.object.pk)
            else:
                messages.error(self.request, 'Formulario no válido')
                return redirect('perfiles:edit', pk=self.object.pk)
                
                
                
        
        elif 'submit_titular_form' in self.request.POST:
            titular_form = TitularForm(self.request.POST)
            if titular_form.is_valid():
                if titular_form.cleaned_data['perro_titular']:
                    # Guardar el formulario titular_form
                    titular_form.save()
                    messages.success(self.request, 'Titularidad - Se ha guardado correctamente')
                    return redirect('perfiles:edit', pk=self.object.pk)
                else:
                    if not titular_form.cleaned_data['titular'] and not titular_form.cleaned_data['perro_titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un titular y un ejemplar')
                        return redirect('perfiles:edit', pk=self.object.pk)
                    elif not titular_form.cleaned_data['perro_titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un ejemplar')
                        return redirect('perfiles:edit', pk=self.object.pk)
                    elif not titular_form.cleaned_data['titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un titular')
                        return redirect('perfiles:edit', pk=self.object.pk)
                        
            else:
                messages.error(self.request, 'Perfil - Formulario no válido')
                return redirect('perfiles:edit', pk=self.object.pk)
        
        else:      
      

            # Obtener el perfil
            perfil = form.save(commit=False)
            # Obtener los datos del usuario
            usuario_form = UsuarioForm(self.request.POST, instance=perfil.user)
            # Guardar los datos del usuario
            usuario_form.save()
            # Guardar el perfil
            perfil.save()
            messages.success(self.request, 'Perfil - Se ha guardado correctamente')
            return redirect('perfiles:detail', pk=perfil.pk)

            





@method_decorator(staff_member_required, name='dispatch')
class DelegacionCreate(CreateView):
    model = Delegacion
    form_class = DelegacionForm
    success_url = reverse_lazy('delegaciones:delegaciones')


    

@method_decorator(staff_member_required, name='dispatch')
class AfijoCreate(CreateView):
    model = Afijo
    form_class = AfijoForm
    success_url = reverse_lazy('afijos:afijos')