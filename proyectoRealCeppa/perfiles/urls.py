from django.urls import path
from .views import PerfilListView, PerfilDetailView, DelegacionCreate, AfijoCreate, PerfilUpdateView

perfiles_patterns = ([
    path('', PerfilListView.as_view(), name='list'),
    path('<int:pk>/', PerfilDetailView.as_view(), name='detail'),
    path('editar/<int:pk>/', PerfilUpdateView.as_view(), name='edit'),
    path('delegacion', DelegacionCreate.as_view(), name='create'),

    path('profile/Afijo', AfijoCreate.as_view(), name='create'),
], "perfiles")
