from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm, TitularForm, CesionarioForm, UsuarioForm, PerfilUsuarioForm
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.urls import reverse_lazy
from django import forms
from perfiles.models import Perfil
from perros.models import  Titular, Cesionario
from messenger.models import Message, Thread
#import render
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect


class StaffRequiredMixin(object):
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        #get the pk of the user created
        pk = self.object.pk
        #get perfil 
        perfil = Perfil.objects.get(user_id=pk)
        #return to perfiles + perfil id
        return reverse_lazy('perfiles:edit', kwargs={'pk':perfil.pk}) + '?register'
        #return reverse_lazy('login') + '?register'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()
        #Modificar en tiempo de ejecución
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario', 'required':True})
        form.fields['first_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre', 'required':True})
        form.fields['last_name'].widget = forms.TextInput(attrs={'class':'form-control', 'placeholder':'Apellido', 'required':True})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email', 'required':True})
        form.fields['is_staff'].widget = forms.CheckboxInput(attrs={ 'placeholder':'Administrador', 'required':True})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña', 'required':True})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Repita la contraseña', 'required':True})

        return form

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


@method_decorator(login_required, name='dispatch')
class ProfileUpdate(UpdateView):
    model = Perfil
    template_name = 'registration/profile_form.html'
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

    def get_object(self):
        #recuperar el objeto 'Perfil' que se va a editar ya que aquí solo tenemos el usuario
        profile, created =  Perfil.objects.get_or_create(user=self.request.user)
        return profile
    
    def get_context_data(self, **kwargs):
        # Llamamos al método padre para obtener el contexto por defecto
        context = super().get_context_data(**kwargs)
        current_titular = Titular.objects.filter(titular=self.object.user)
        context['current_titular'] = current_titular
        current_cesionario = Cesionario.objects.filter(cesionario=self.object.user)
        context['current_cesionario'] = current_cesionario
        context.update({
            'perfil_form': ProfileForm(**self.get_form_kwargs()),
            'usuario_form':UsuarioForm(**self.get_form_kwargs()),
            'titular_form': TitularForm(**self.get_form_kwargs()),
            'cesionario_form': CesionarioForm(**self.get_form_kwargs()),
        })
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

    def form_valid(self, form):

        
        if 'submit_cesionario_form' in self.request.POST:
            cesionario_form = CesionarioForm(self.request.POST)
            if cesionario_form.is_valid():
                if cesionario_form.cleaned_data['cesionario'] and cesionario_form.cleaned_data['perro_cesionario']:
                    # Guardar el formulario cesionario_form
                    cesionario_form.save()
                    messages.success(self.request, 'Cesión - Se ha guardado correctamente')
                    return redirect('my-profile')
                else:
                    if not cesionario_form.cleaned_data['cesionario'] and not cesionario_form.cleaned_data['perro_cesionario']:
                        messages.error(self.request, 'Cesión - Debe seleccionar un cesionario y un ejemplar')
                        return redirect('profile')
                    elif not cesionario_form.cleaned_data['cesionario']:                        
                        messages.error(self.request, 'Cesión - Debe seleccionar un cesionario')
                        return redirect('profile')
                    elif not cesionario_form.cleaned_data['perro_cesionario']:
                        messages.error(self.request, 'Cesión - Debe seleccionar un ejemplar')
                        return redirect('profile')
            else:
                messages.error(self.request, 'Formulario no válido')
                return redirect('profile')
                
                
                
        
        elif 'submit_titular_form' in self.request.POST:
            titular_form = TitularForm(self.request.POST)
            if titular_form.is_valid():
                if titular_form.cleaned_data['perro_titular']:
                    # Guardar el formulario titular_form
                    titular_form.save()
                    messages.success(self.request, 'Titularidad - Se ha guardado correctamente')
                    return redirect('my-profile')
                else:
                    if not titular_form.cleaned_data['titular'] and not titular_form.cleaned_data['perro_titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un titular y un ejemplar')
                        return redirect('profile')
                    elif not titular_form.cleaned_data['perro_titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un ejemplar')
                        return redirect('profile')
                    elif not titular_form.cleaned_data['titular']:
                        messages.error(self.request, 'Titularidad - Debe seleccionar un titular')
                        return redirect('profile')
                        
            else:
                messages.error(self.request, 'Perfil - Formulario no válido')
                return redirect('profile')
        
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
            return redirect('my-profile')
        

@method_decorator(login_required, name='dispatch')
class EmailUpdate(UpdateView):
    form_class = EmailForm
    success_url = reverse_lazy('profile')
    template_name = 'registration/profile_email_form.html'

    def get_object(self):
        #Recuperar el objeto que se va a editar arriba
        return self.request.user

    def get_form(self, form_class=None):
        form = super(EmailUpdate, self).get_form()
        #Modificar en tiempo de ejecución
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2', 'placeholder':'Email'})
        return form

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

@method_decorator(login_required, name='dispatch')  
class MiPerfil(TemplateView):
    template_name = 'registration/my_profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        #obtener perfil a partir del usaurio logueado
        perfil = Perfil.objects.get(user=request.user)
        #obtener perfil a partir del usuario logueado
        perfiles = Perfil.objects.all()
        # Obtener mensajes no leídos
        messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
        # Obtener hilos a partir de mensajes
        threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
        # Contar hilos
        unread_messages = threads.count()

        unreaded_messages = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).count()
        id_unread_threads = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).values_list('thread', flat=True).distinct()

        current_titular = Titular.objects.filter(titular=self.request.user)
        current_cesionario = Cesionario.objects.filter(cesionario=self.request.user)

        return render(request, self.template_name, { 'perfil': perfil, 'user': user, 'unread_messages': unread_messages, 'unreaded_messages': unreaded_messages, 'id_unread_threads': id_unread_threads, 'threads': threads,
        'perfiles': perfiles, 'current_titular': current_titular, 'current_cesionario': current_cesionario })
