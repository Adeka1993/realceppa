from django.urls import path
from  .views import HomePageView, SobreNosotrosPageView, ContactanosPageView
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', HomePageView.as_view(), name="home"), 
    path(_('sobreNosotros/'), SobreNosotrosPageView.as_view(), name="sobreNosotros"),
    path(_('contactanos/'), ContactanosPageView.as_view(), name="contactanos"),   
]

