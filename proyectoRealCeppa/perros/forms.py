from django import forms
from .models import Perro, Salto, Camada, LOPerro, SexoPerro, ColorMarcas, EstadoPerro, TipoPelo, Afijo, TipoCPR, EstadoCPR
from .models import Camada, HDRadio, EDRadio, ADNPerro, KorungTipo, PeticionSalto, ValidacionSalto
from registration.models import User

class PerroForm(forms.ModelForm):
    

    lo = forms.ModelChoiceField(queryset=LOPerro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Libro de Origenes")
    sexo = forms.ModelChoiceField(queryset=SexoPerro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Sexo *")
    estadoPerro =forms.ModelChoiceField(queryset=EstadoPerro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Estado")
    tipoPelo =forms.ModelChoiceField(queryset=TipoPelo.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tipo Pelo")
    colorMarcas =forms.ModelChoiceField(queryset=ColorMarcas.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Color Marcas")
    afijo =forms.ModelChoiceField(queryset=Afijo.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Afijo")
    tipoCPR = forms.ModelChoiceField(queryset=TipoCPR.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tipo CPR")
    estadoCPR = forms.ModelChoiceField(queryset=EstadoCPR.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Estado CPR")
    padre = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Padre")
    madre = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Madre")
    camada = forms.ModelChoiceField(queryset=Camada.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Camada")
    hdRadio = forms.ModelChoiceField(queryset=HDRadio.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="HD Radio")
    edRadio = forms.ModelChoiceField(queryset=EDRadio.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="ED Radio")
    adn = forms.ModelChoiceField(queryset=ADNPerro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="ADN")
    korungTipo = forms.ModelChoiceField(queryset=KorungTipo.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Korung Tipo")
    
    class Meta:
        model = Perro
        fields = ['nombre','lo', 'nlo', 'tatuaje','chip','sexo','fechaNacimiento','estadoPerro','tipoPelo', 'colorMarcas', 'afijo','origenLibrosExt',
        'tipoCPR','estadoCPR','fechaAptitudCria','fechaSeleccionCria','fechaBasicoCria','padre','madre','camada','hdRadio', 'edRadio', 'adn','korungTipo'
        ,'korungAnys','zb','fechaHabCamadaOcasional','korungInforme','observaciones',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'nlo': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Libro Origenes'}),
            'tatuaje': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Tatuaje'}),
            'chip': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Chip '}),
            'fechaNacimiento': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'origenLibrosExt': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'fechaAptitudCria': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechaSeleccionCria': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechaBasicoCria': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'korungAnys': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Korung Anys'}),
            'korungInforme':forms.Textarea(attrs={'class':'form-control', 'rows':1, 'placeholder':'Korung Informe'}),
            'zb': forms.TextInput(attrs={'class':'form-control', 'placeholder':'ZB'}),
            'fechaHabCamadaOcasional': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'observaciones':forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Observaciones'}),
        }
        labels = {
            'nombre':'Nombre *', 'nlo':'Nº Libro Origenes', 'tatuaje':'Tatuaje', 'chip':'Chip *', 'fechaNacimiento':'Fecha Nacimiento *', 
            'origenLibrosExt':'Origen Libros Ext.', 'fechaAptitudCria':'Fecha Aptitud Cría', 'fechaSeleccionCria':'Fecha Seleccion Cría'
            ,'fechaBasicoCria':'Fecha Básico Cría', 'korungAnys':'Korung Anys','korungInforme':'Korung Informe','zb':'ZB'
            ,'fechaHabCamadaOcasional':'Fecha Hab. Camada Ocasional','observaciones':'Observaciones'
           
        }

    #NOT REQUIRED
    def __init__(self, *args, **kwargs):
        super(PerroForm, self).__init__(*args, **kwargs)
        self.fields['lo'].required = False
        self.fields['chip'].required = True
        self.fields['fechaNacimiento'].required = True
        self.fields['nlo'].required = False
        self.fields['tatuaje'].required = False
        self.fields['estadoPerro'].required = False
        self.fields['tipoPelo'].required = False
        self.fields['colorMarcas'].required = False
        self.fields['afijo'].required = False
        self.fields['origenLibrosExt'].required = False
        self.fields['tipoCPR'].required = False
        self.fields['estadoCPR'].required = False
        self.fields['fechaAptitudCria'].required = False
        self.fields['fechaSeleccionCria'].required = False
        self.fields['fechaBasicoCria'].required = False
        self.fields['padre'].required = False
        self.fields['madre'].required = False
        self.fields['camada'].required = False
        self.fields['hdRadio'].required = False
        self.fields['edRadio'].required = False
        self.fields['adn'].required = False
        self.fields['korungTipo'].required = False
        self.fields['korungAnys'].required = False
        self.fields['korungInforme'].required = False
        self.fields['zb'].required = False
        self.fields['fechaHabCamadaOcasional'].required = False
        self.fields['observaciones'].required = False

    

class SaltoForm(forms.ModelForm):

    peticionSalto = forms.ModelChoiceField(queryset=PeticionSalto.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Petición Salto")
    validacionSalto = forms.ModelChoiceField(queryset=ValidacionSalto.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Validación Salto")
    socio = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Socio")
    hembra = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Hembra")
    macho = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Macho")
    afijo = forms.ModelChoiceField(queryset=Afijo.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Afijo")
    
    class Meta:
        model = Salto
        fields = ['validacionSalto', ]
        widgets = {
            'fechaSalto': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechaComunicacion': forms.DateInput(attrs={'type':'date','class':'form-control'}),
        }
        labels = {
            'fechaSalto':'Fecha Salto','fechaComunicacion':'Fecha Comunicacion',
        }

#Formulario a partir del modelo Camada
class CamadaForm(forms.ModelForm):

    afijo = forms.ModelChoiceField(queryset=Afijo.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Afijo")
    criador = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Criador")
    salto = forms.ModelChoiceField(queryset=Salto.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Salto")
    class Meta:
        model = Camada
        fields = ['salto', 'fechaCamada', 'fechaComunicacion', 'NHTotales', 'NMTotales', 'NHNacidosMuertos', 
        'NMNacidosMuertos', 'NHMuertosPost', 'NMMuertosPost', 'NHInsCPR', 'NMInsCPR','NHVarCompr','NMVarCompr',
         'fechaInspeccion','buenEstadoMadre','BEMIncidencias','buenEstadoCachorros','BECIncidencias','observaciones','fechaEnvioEmailDelegacion']
        widgets = {
            'fechaCamada': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechaComunicacion': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'NHTotales': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Hembra Totales'}),
            'NMTotales': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Macho Totales'}),
            'NHNacidosMuertos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Hembra Nacidos Muertos'}),
            'NMNacidosMuertos': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Macho Nacidos Muertos'}),
            'NHMuertosPost': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Hembra Muertos Post'}),
            'NMMuertosPost': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Macho Muertos Post'}),
            'NHInsCPR': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Hembra Ins. CPR'}),
            'NMInsCPR': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Macho Ins. CPR'}),
            'NHVarCompr': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Hembra Var. Compr.'}),
            'NMVarCompr': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nº Macho Var. Compr.'}),
            'fechaInspeccion': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'buenEstadoMadre': forms.CheckboxInput(attrs={'class':'form-control'}),
            'BEMIncidencias': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Incidencias'}),
            'buenEstadoCachorros': forms.CheckboxInput(attrs={'class':'form-control'}),
            'BECIncidencias': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Incidencias'}),
            'observaciones': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Observaciones'}),
            'fechaEnvioEmailDelegacion': forms.DateInput(attrs={'type':'date','class':'form-control'}),

        }
        labels = {
            'fechaCamada':'Fecha Camada','fechaComunicacion':'Fecha Comunicacion','NHTotales':'Nº Hembra Totales',
            'NMTotales':'Nº Macho Totales','NHNacidosMuertos':'Nº Hembra Nacidos Muertos','NMNacidosMuertos':'Nº Macho Nacidos Muertos',
            'NHMuertosPost':'Nº Hembra Muertos Post','NMMuertosPost':'Nº Macho Muertos Post','NHInsCPR':'Nº Hembra Ins. CPR',
            'NMInsCPR':'Nº Macho Ins. CPR','NHVarCompr':'Nº Hembra Var. Compr.','NMVarCompr':'Nº Macho Var. Compr.',
            'fechaInspeccion':'Fecha Inspeccion','buenEstadoMadre':'Buen Estado Madre','BEMIncidencias':'Incidencias',
            'buenEstadoCachorros':'Buen Estado Cachorros','BECIncidencias':'Incidencias','observaciones':'Observaciones',
            'fechaEnvioEmailDelegacion':'Fecha Envio Email Delegacion',
        }   
        