from django.urls import path
from .views import PerroDetailView, PerroListView, PerroCreate, PerroUpdate, PerroDelete,PerroDetailPDFV, PerroDetailPDFV2
from .views import SaltoDetailView, SaltoListView, SaltoCreate, SaltoUpdate, SaltoDelete
from .views import CamadaDetailView, CamadaListView, CamadaCreate, CamadaUpdate, CamadaDelete, SearchResultView


perros_patterns = ([
    path('', PerroListView.as_view(), name='perros'),
    #url input search perros
    path('search/', SearchResultView.as_view(), name='perro_search'),

    path('<int:pk>/', PerroDetailView.as_view(), name='perro'),
    path('<int:pk>/pedigree', PerroDetailPDFV.as_view(), name='perro_pedigree'),
    path('<int:pk>/pedigree2', PerroDetailPDFV2.as_view(), name='perro_pedigree2'),


    path('create/', PerroCreate.as_view(), name='perroCreate'),
    path('update/<int:pk>/', PerroUpdate.as_view(), name='perroUpdate'),
    path('delete/<int:pk>/', PerroDelete.as_view(), name='perroDelete'),


],'perros')






saltos_patterns = ([
    path('', SaltoListView.as_view(), name='saltos'),
    path('search/', SearchResultView.as_view(), name='salto_search'),
    path('<int:pk>/', SaltoDetailView.as_view(), name='salto'),
    path('create/', SaltoCreate.as_view(), name='saltoCreate'),
    path('update/<int:pk>/', SaltoUpdate.as_view(), name='saltoUpdate'),
    path('delete/<int:pk>/', SaltoDelete.as_view(), name='saltoDelete'),

],'saltos')

camadas_patterns = ([
    path('', CamadaListView.as_view(), name='camadas'),
    path('search/', SearchResultView.as_view(), name='camada_search'),
    path('<int:pk>/', CamadaDetailView.as_view(), name='camada'),
    path('create/', CamadaCreate.as_view(), name='camadaCreate'),
    path('update/<int:pk>/', CamadaUpdate.as_view(), name='camadaUpdate'),
    path('delete/<int:pk>/', CamadaDelete.as_view(), name='camadaDelete'),

],'camadas')