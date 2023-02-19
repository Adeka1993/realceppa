import django
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from .models import Message, Thread
from django.http import Http404, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy 
from perfiles.models import Perfil
from django.shortcuts import render
from django.db.models import Count, Q


# Create your views here.

@method_decorator(login_required, name="dispatch")
class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        perfiles = Perfil.objects.all()
        context["users"] = users
        context["perfiles"] = perfiles
        context["perfil"] = Perfil.objects.get(user=self.request.user)
        unread_messages = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).count()
        id_unread_threads = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).values_list('thread', flat=True).distinct()
        context["id_unread_threads"] = id_unread_threads
        context["unread_messages"] = unread_messages
    
        return context
    #lo comentado realiza lo mismo que la línea superior
    #model = Thread

    #def get_queryset(self):
    #    queryset = super(ThreadList, self).get_queryset()
    #    return queryset.filter(users=self.request.user)

@method_decorator(login_required, name="dispatch")
class ThreadDetail(DetailView):
    model = Thread
    #change readed property to True of messages
    def get(self, request, *args, **kwargs):
        messages = self.get_object().messages.all()
        for message in messages:
            if message.user != self.request.user:
                message.readed = True
                message.save()
        return super(ThreadDetail, self).get(request, *args, **kwargs)

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = User.objects.all()
        perfiles = Perfil.objects.all()
        context["users"] = users
        context["perfiles"] = perfiles
        context["perfil"] = Perfil.objects.get(user=self.request.user)
        unread_messages = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).count()
        id_unread_threads = Message.objects.filter(thread__users=self.request.user, readed=False).exclude(user=self.request.user).values_list('thread', flat=True).distinct()
        context["id_unread_threads"] = id_unread_threads
        context["unread_messages"] = unread_messages
    
        return context



def add_message(request, pk):
    json_response={'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content',None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created']=True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User is not authenticated")
    
    return JsonResponse(json_response)

@login_required
def start_thread(request, pk):
    user = get_object_or_404(User, pk=pk)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))
