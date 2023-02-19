from django.views.generic.list import ListView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse, reverse_lazy
from .models import Perro, Salto, Camada, EstadoPerro, ValidacionSalto
from .forms import PerroForm, SaltoForm, CamadaForm

from django.http import HttpResponse
from .utils import render_to_pdf
from django.template.loader import get_template
from io import BytesIO
from xhtml2pdf import pisa
from perfiles.models import Perfil
from messenger.models import Message, Thread

import os
from django.conf import settings
from django import template

register = template.Library()

@register.filter
def replace_filter(value, args):
    return value.replace(args[0], args[1])

    


class StaffRequiredMixin(object):

    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)



# Create your views here.

#PERROS
@method_decorator(staff_member_required, name='dispatch')
class PerroListView(ListView):
    model = Perro 
    paginate_by = 9
    #llennar lista de estados perros
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = EstadoPerro.objects.all()
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
    


@method_decorator(staff_member_required, name='dispatch')
class SearchResultView(ListView):
    model = Perro
    paginate_by = 9
    #llennar lista de estados perros
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estados'] = EstadoPerro.objects.all()
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

    def get_queryset(self,*args,**kwargs):
        
        queryNombreAfijo = self.request.GET.get('name')
        queryChip = self.request.GET.get('chip')
        queryNLO = self.request.GET.get('nlo')
        queryTatuaje = self.request.GET.get('tatuaje')

        #get value crom multiple select separatef by comma if not empty and not value=0
        queryEstadoPerro = self.request.GET.get('estadoPerro')

        queryPadre = self.request.GET.get('padre')
        queryMadre = self.request.GET.get('madre')


        object_list = Perro.objects.all()

        if queryNombreAfijo:
            object_list = object_list.filter(
                nombre__icontains=queryNombreAfijo,) | Perro.objects.filter(
                afijo__nombre__icontains=queryNombreAfijo)

        if queryChip:
            object_list = object_list.filter(
                chip__icontains=queryChip,)

        if queryNLO:
            object_list = object_list.filter(
                nlo__icontains=queryNLO,) | Perro.objects.filter(
                lo__descripcion__icontains=queryNLO)

        if queryTatuaje:
            object_list = object_list.filter(
                tatuaje__icontains=queryTatuaje,)

        if queryEstadoPerro:
            object_list = object_list.filter(
                estadoPerro__in=queryEstadoPerro)

        if queryPadre:
            object_list = object_list.filter(
                padre__nombre__icontains=queryPadre,) | Perro.objects.filter(
                padre__afijo__nombre__icontains=queryPadre)

        if queryMadre:
            object_list = object_list.filter(
                madre__nombre__icontains=queryMadre,) | Perro.objects.filter(
                madre__afijo__nombre__icontains=queryMadre)


        return object_list
   


@method_decorator(staff_member_required, name='dispatch')
class PerroDetailView(DetailView):
    model = Perro
    form_class = PerroForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
        

def fetch_resources(uri, rel):
    # Configurar el directorio de recursos a utilizar
    path = os.path.join(settings.MEDIA_ROOT, uri.replace(settings.MEDIA_URL, ""))

    # Si el recurso existe en el directorio especificado, devolverlo
    if os.path.exists(path):
        return path

    # Si el recurso no existe, devolver una cadena vacía
    return ""





def generate_pdf(template_src, context_dict):
    # Obtener una instancia de la plantilla HTML especificada
    template = get_template(template_src)

    # Renderizar la plantilla HTML utilizando el diccionario de contexto dado y obtener el contenido HTML generado
    html = template.render(context_dict)

    # Generar el PDF utilizando el contenido HTML generado
    response = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), response, link_callback=fetch_resources)

    # Devolver el PDF generado como una cadena de bytes
    return response.getvalue()

@method_decorator(staff_member_required, name='dispatch')
class PerroDetailPDFV(View):
    def get(self, request, *args, **kwargs):
        perro = Perro.objects.get(pk=self.kwargs['pk'])
        camada = perro.camada
        direccion = ""
        codigo_postal = ""
        poblacion = ""

        if camada is None:
            criador = None
            perfilCriador = None
        else:
            if camada.criador is None:
                criador = None
                perfilCriador = None

                direccion = ""
                codigo_postal = ""
                poblacion = ""
            else:
                criador = camada.criador
                perfilCriador = Perfil.objects.get(user=criador)

                if perfilCriador.direccion is None:
                    direccion = ""
                else:
                    direccion = perfilCriador.direccion.replace(" ", "&nbsp")

                if perfilCriador.codigoPostal is None:
                    codigo_postal = ""
                else:
                    codigo_postal = perfilCriador.codigoPostal.replace(" ", "&nbsp")

                if perfilCriador.poblacion is None:
                    poblacion = ""
                else:
                    poblacion = perfilCriador.poblacion.replace(" ", "&nbsp")

        

        data = {'perro': perro, 'STATIC_ROOT_PEDIGREE': settings.STATIC_ROOT_PEDIGREE, 'FONDO' :'position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: -1;',
                'criador': criador, 'perfilCriador': perfilCriador,'direccion': direccion, 'codigo_postal': codigo_postal, 'poblacion': poblacion}

        pdf = generate_pdf('perros/perro_pedigree.html', data)

        return HttpResponse(pdf, content_type='application/pdf')


@method_decorator(staff_member_required, name='dispatch')
class PerroDetailPDFV2(View):
    def get(self, request, *args, **kwargs):
        perro = Perro.objects.get(pk=self.kwargs['pk'])
        camada = perro.camada
        direccion = ""
        codigo_postal = ""
        poblacion = ""


        if camada is None:
            criador = None
            perfilCriador = None
        else:
            if camada.criador is None:
                criador = None
                perfilCriador = None
            else:
                criador = camada.criador
                perfilCriador = Perfil.objects.get(user=criador)

                if perfilCriador.direccion is None:
                    direccion = ""
                else:
                    direccion = perfilCriador.direccion.replace(" ", "&nbsp")

                if perfilCriador.codigoPostal is None:
                    codigo_postal = ""
                else:
                    codigo_postal = perfilCriador.codigoPostal.replace(" ", "&nbsp")

                if perfilCriador.poblacion is None:
                    poblacion = ""
                else:
                    poblacion = perfilCriador.poblacion.replace(" ", "&nbsp")



        data = {'perro': perro, 'STATIC_ROOT_PEDIGREE': settings.STATIC_ROOT_PEDIGREE, 'FONDO' :'position: absolute;top: 0;left: 0;width: 100%;height: 100%;z-index: -1;',
                'criador': criador, 'perfilCriador': perfilCriador,'direccion': direccion, 'codigo_postal': codigo_postal, 'poblacion': poblacion}

        pdf = generate_pdf('perros/perro_pedigree2.html', data)

        return HttpResponse(pdf, content_type='application/pdf')




@method_decorator(staff_member_required, name='dispatch')
class PerroCreate(CreateView):
    model = Perro
    form_class = PerroForm
    success_url = reverse_lazy('perros:perros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

@method_decorator(staff_member_required, name='dispatch')
class PerroUpdate(UpdateView):
    model = Perro
    form_class = PerroForm
    template_name_suffix = '_update_form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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

    def get_success_url(self):
        return reverse_lazy('perros:perroUpdate', args=[self.object.id]) + '?ok'


@method_decorator(staff_member_required, name='dispatch')
class PerroDelete(DeleteView):
    model = Perro
    success_url = reverse_lazy('perros:perros')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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






#SALTOS
@method_decorator(staff_member_required, name='dispatch')
class SaltoListView(ListView):
    model = Salto
    paginate_by = 9
    #llennar lista de estados perros
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['validacion'] = ValidacionSalto.objects.all()
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



@method_decorator(staff_member_required, name='dispatch')
class SearchSaltosResultView(ListView):
    model = Salto
    paginate_by = 9
    #llennar lista de Validaciones de salto
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['validaciones'] = ValidacionSalto.objects.all()
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

    def get_queryset(self,*args,**kwargs):

        #get value from search form
        queryIdSalto = self.request.GET.get('idSalto')
        queryIdPeticion = self.request.GET.get('idPeticion')
        queryValidacion = self.request.GET.get('validacion')
        querySocio = self.request.GET.get('socio')
        queryFechaSalto = self.request.GET.get('fechaSalto')
        queryFechaValidacion = self.request.GET.get('fechaValidacion')
        queryHembra = self.request.GET.get('hembra')
        queryMacho = self.request.GET.get('macho')
        queryAfijo = self.request.GET.get('afijo')
        
        queryNombreAfijo = self.request.GET.get('name')
        queryChip = self.request.GET.get('chip')
        queryNLO = self.request.GET.get('nlo')
        queryTatuaje = self.request.GET.get('tatuaje')


        object_list = Salto.objects.all()

        if queryIdSalto:
            object_list = object_list.filter(
                idSalto__icontains=queryIdSalto,)
        if queryIdPeticion:
            object_list = object_list.filter(
                idPeticion__icontains=queryIdPeticion,)
        if queryValidacion:
            object_list = object_list.filter(
                validacion__in=queryValidacion,)
        if querySocio:
            object_list = object_list.filter(
                socio__nombre__icontains=querySocio,)
        if queryFechaSalto:
            object_list = object_list.filter(
                fechaSalto__icontains=queryFechaSalto,)
        if queryFechaValidacion:
            object_list = object_list.filter(
                fechaValidacion__icontains=queryFechaValidacion,)
        if queryHembra:
            object_list = object_list.filter(
                hembra__icontains=queryHembra,) | Salto.objects.filter(
                hembra__afijo__nombre__icontains=queryHembra)
        if queryMacho:
            object_list = object_list.filter(
                macho__nombre__icontains=queryMacho,) | Salto.objects.filter(
                macho__afijo__nombre__icontains=queryMacho)
        if queryAfijo:
            object_list = object_list.filter(
                afijo__nombre__icontains=queryAfijo,)


        return object_list

@method_decorator(staff_member_required, name='dispatch')
class SaltoDetailView(DetailView):
    model = Salto

@method_decorator(staff_member_required, name='dispatch')
class SaltoCreate(CreateView):
    model = Salto
    form_class = SaltoForm
    success_url = reverse_lazy('saltos:saltos')


@method_decorator(staff_member_required, name='dispatch')
class SaltoUpdate(UpdateView):
    model = Salto
    form_class = SaltoForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('saltos:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class SaltoDelete(DeleteView):
    model = Salto
    success_url = reverse_lazy('saltos:saltos')




#CAMADAS
@method_decorator(staff_member_required, name='dispatch')
class CamadaListView(ListView):
    model = Camada

@method_decorator(staff_member_required, name='dispatch')
class CamadaDetailView(DetailView):
    model = Camada

@method_decorator(staff_member_required, name='dispatch')
class CamadaCreate(CreateView):
    model = Camada
    form_class = CamadaForm
    success_url = reverse_lazy('camadas:camadas')


@method_decorator(staff_member_required, name='dispatch')
class CamadaUpdate(UpdateView):
    model = Camada
    form_class = CamadaForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('camadas:update', args=[self.object.id]) + '?ok'

@method_decorator(staff_member_required, name='dispatch')
class CamadaDelete(DeleteView):
    model = Camada
    success_url = reverse_lazy('camadas:delete')

