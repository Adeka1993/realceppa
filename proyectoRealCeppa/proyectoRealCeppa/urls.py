"""proyectoRealCeppa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from perros.urls import perros_patterns, saltos_patterns, camadas_patterns
from perfiles.urls import perfiles_patterns
from messenger.urls import messenger_patterns
#from general.urls import general_patterns
from django.conf import settings
from django.utils.translation import gettext_lazy as _


from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
]
urlpatterns+=i18n_patterns(
    path('',include('core.urls')),
    path(_('perros/'),include(perros_patterns)),
    path(_('saltos/'),include(saltos_patterns)),
    path(_('camadas/'),include(camadas_patterns)),
    # Paths de Auth
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    # Paths de profiles
    path('perfiles/', include(perfiles_patterns)),
    path('messenger/', include(messenger_patterns)),
    #path('general/', include(general_patterns)),
)

if 'rosetta' in settings.INSTALLED_APPS:
    urlpatterns += [
        re_path(r'^rosetta/', include('rosetta.urls'))
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
