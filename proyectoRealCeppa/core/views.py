
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.translation import gettext_lazy as _
from django.utils.translation import get_language, activate
from perfiles.models import Perfil
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
#import Messages
from messenger.models import Message, Thread


def home(request):
    

    return render(request, 'core/home.html')



#def translate(language):
    cur_language = get_language()
    try:
        activate(language)
        text = _('hola')
    finally:
        activate(cur_language)
    return text


class BaseView(TemplateView):
    template_name = "core/base.html"

    def get(self, request, *args, **kwargs):   
        if request.user.is_authenticated:

            #obtener perfil a partir del usuario logueado
            perfil = Perfil.objects.get(user=request.user)
            # Obtener mensajes no leídos
            messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
            # Obtener hilos a partir de mensajes
            threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
            # Contar hilos
            unread_messages = threads.count()

            
            return render(request, self.template_name, {'perfil': perfil, 'unread_messages': unread_messages})
        else:
            return render(request, self.template_name)
    




class HomePageView(TemplateView):
    template_name = "core/home.html"

    def get(self, request, *args, **kwargs):   
        if request.user.is_authenticated:

            #obtener perfil a partir del usuario logueado
            perfil = Perfil.objects.get(user=request.user)
            # Obtener mensajes no leídos
            messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
            # Obtener hilos a partir de mensajes
            threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
            # Contar hilos
            unread_messages = threads.count()

            
            return render(request, self.template_name, {'perfil': perfil, 'unread_messages': unread_messages})
        else:
            return render(request, self.template_name)

 
        

class SobreNosotrosPageView(TemplateView):
    template_name = "core/sobreNosotros.html"
    
    def get(self, request, *args, **kwargs):   
        if request.user.is_authenticated:

            #obtener perfil a partir del usuario logueado
            perfil = Perfil.objects.get(user=request.user)
            # Obtener mensajes no leídos
            messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
            # Obtener hilos a partir de mensajes
            threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
            # Contar hilos
            unread_messages = threads.count()

            
            return render(request, self.template_name, {'perfil': perfil, 'unread_messages': unread_messages})
        else:
            return render(request, self.template_name)


class ContactanosPageView(TemplateView):
    template_name = "core/contactanos.html"

    def get(self, request, *args, **kwargs):   
        if request.user.is_authenticated:

            #obtener perfil a partir del usuario logueado
            perfil = Perfil.objects.get(user=request.user)
            # Obtener mensajes no leídos
            messages = Message.objects.filter(readed=False).exclude(user=self.request.user)
            # Obtener hilos a partir de mensajes
            threads = Thread.objects.filter(users=self.request.user, messages__in=messages).distinct()
            # Contar hilos
            unread_messages = threads.count()

            
            return render(request, self.template_name, {'perfil': perfil, 'unread_messages': unread_messages})
        else:
            return render(request, self.template_name)