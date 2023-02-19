from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from perfiles.models import Perfil
from django.views.generic import View
#import render y redirect
from django.shortcuts import render, redirect
from perros.models import Perro, Titular, Cesionario
from perfiles.models import Afijo, Delegacion , Perfil, TipoSocio, GrupoTrabajo, MotivoBajaUsuario
from perfiles.models import Tratamiento, Provincia, Region, Pais, TipoSocio, Delegacion, MotivoBajaUsuario

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User 
        fields = ("username", "first_name", "last_name", "email", "is_staff", "password1", "password2")




    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email introducido ya existe, introduzca uno diferente.")
        return email






class TitularForm(forms.ModelForm):

    titular = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Titular")
    perro_titular = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Perro")
    class Meta:
        model = Titular
        fields = ['titular', 'perro_titular', 'fechaInicio', 'fechaFin']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {

            'fechaInicio': 'Fecha de Inicio',
            'fechaFin': 'Fecha de Fin',
        }

    #NOT REQUIRED
    #NOT REQUIRED
    def __init__(self, *args, **kwargs):
        super(TitularForm, self).__init__(*args, **kwargs)
        self.fields['titular'].required = False
        self.fields['perro_titular'].required = False
        self.fields['titular'].initial = self.instance
     




 


class CesionarioForm(forms.ModelForm):
    cesionario = forms.ModelChoiceField(queryset=User.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Cesionario")
    perro_cesionario = forms.ModelChoiceField(queryset=Perro.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Perro")
    class Meta:
        model = Cesionario
        fields = ['cesionario', 'perro_cesionario', 'fechaInicio', 'fechaFin']
        widgets = {
            'fechaInicio': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'fechaFin': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }
        labels = {

            'fechaInicio': 'Fecha de Inicio',
            'fechaFin': 'Fecha de Fin',
        }
    def __init__(self, *args, **kwargs):
        super(CesionarioForm, self).__init__(*args, **kwargs)
        self.fields['cesionario'].required = False
        self.fields['perro_cesionario'].required = False
        self.fields['cesionario'].initial = self.instance

class ProfileForm(forms.ModelForm):

    tratamiento = forms.ModelChoiceField(queryset=Tratamiento.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tratamiento")
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Provincia")
    region = forms.ModelChoiceField(queryset=Region.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Region")
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Pais")
    tipoSocio = forms.ModelChoiceField(queryset=TipoSocio.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tipo de Socio")
    delegacion = forms.ModelChoiceField(queryset=Delegacion.objects.all(),empty_label="Desconocido",required=False,  widget=forms.Select(attrs={'class':'form-control'}), label="Delegacion")
    grupoTrabajo = forms.ModelChoiceField(queryset=GrupoTrabajo.objects.all(),empty_label="Desconocido", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Grupo de Trabajo")
    afijo = forms.ModelChoiceField(queryset=Afijo.objects.all(),empty_label="Desconocido", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Afijo")
    
    criador = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Criador")
    figurante = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Figurante")
    trazador = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Trazador")
    juez = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Juez")
    inspector = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Inspector")
    faltaPago = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Falta Pago")
    motivoBajaUsuario = forms.ModelChoiceField(queryset=MotivoBajaUsuario.objects.all(),empty_label="", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Motivo Baja")

    class Meta:
        model = Perfil
        fields = ['tratamiento', 'biografia','direccion','telefono','avatar','dni','numeroSocio','codigoPostal', 'poblacion', 'provincia', 'region', 'pais', 'tipoSocio', 'fechaNacimiento',
        'cuentaBancaria','delegacion','grupoTrabajo','afijo','criador','figurante','trazador','juez','inspector','faltaPago', 'fechaBaja', 'baja', 'motivoBajaUsuario']
        widgets = {
            'biografia': forms.Textarea(attrs={'class':'form-control', 'rows':5, 'placeholder':'Biografia'}),
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'direccion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Direccion'}),
            'telefono': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Telefono'}),
            'avatar':forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'dni': forms.TextInput(attrs={'class':'form-control', 'placeholder':'DNI'}),
            'numeroSocio': forms.TextInput(attrs={'class':'form-control', 'placeholder':'NumeroSocio'}),
            'tratamiento': forms.Select(attrs={'class':'form-control', 'placeholder':'Tratamiento'}),
            'codigoPostal': forms.TextInput(attrs={'class':'form-control', 'placeholder':'CodigoPostal'}),
            'poblacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Poblacion'}),
            'fechaNacimiento': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cuentaBancaria': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Cuenta Bancaria'}),
            'fechaBaja': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'baja': forms.CheckboxInput(attrs={'class':'form-check-input'}),
            #'link': forms.URLInput(attrs={'class':'form-control mt-3',  'placeholder':'Enlace'}),
        }
        labels = {
            'biografia':'Biografia',
            'direccion':'Direccion',
            'telefono':'Telefono',
            'avatar':'Avatar',
            'dni':'DNI',
            'numeroSocio':'NumeroSocio',
            'tramitamiento':'Tratamiento',
            'codigoPostal':'CodigoPostal',
            'poblacion':'Poblacion',
            'fechaNacimiento':'Fecha de Nacimiento',
            'cuentaBancaria':'Cuenta Bancaria',
            'fechaBaja':'Fecha Baja',
            'baja':'Baja',
     

            #'link':'Enlace',
        }

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
            'last_name': forms.TextInput(attrs={'class':'form-control ', 'placeholder':'Apellidos'}),   
            'email': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}),
        }
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellidos',
            'email':'Email',
        }


class PerfilUsuarioForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    email = forms.EmailField(max_length=254, widget=forms.EmailInput(attrs={'class':'form-control'}), label='Email')
    tratamiento = forms.ModelChoiceField(queryset=Tratamiento.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tratamiento")
    provincia = forms.ModelChoiceField(queryset=Provincia.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Provincia")
    region = forms.ModelChoiceField(queryset=Region.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Region")
    pais = forms.ModelChoiceField(queryset=Pais.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Pais")
    tipoSocio = forms.ModelChoiceField(queryset=TipoSocio.objects.all(),empty_label="Desconocido", widget=forms.Select(attrs={'class':'form-control'}), label="Tipo de Socio")
    delegacion = forms.ModelChoiceField(queryset=Delegacion.objects.all(),empty_label="Desconocido", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Delegacion")
    grupoTrabajo = forms.ModelChoiceField(queryset=GrupoTrabajo.objects.all(),empty_label="Desconocido", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Grupo de Trabajo")
    afijo = forms.ModelChoiceField(queryset=Afijo.objects.all(),empty_label="Desconocido", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Afijo")
    criador = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Criador")
    figurante = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Figurante")
    trazador = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Trazador")
    juez = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Juez")
    inspector = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Inspector")
    faltaPago = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class':'form-check-input'}), label="Falta Pago")
    motivoBajaUsuario = forms.ModelChoiceField(queryset=MotivoBajaUsuario.objects.all(),empty_label="", required=False, widget=forms.Select(attrs={'class':'form-control'}), label="Motivo Baja")

    class Meta:      

        model = Perfil
        fields = ['biografia', 'direccion', 'telefono', 'avatar', 'dni', 'numeroSocio','tratamiento', 'codigoPostal', 'poblacion', 'provincia', 'region', 'pais', 'tipoSocio', 'fechaNacimiento',
        'cuentaBancaria', 'delegacion', 'grupoTrabajo', 'afijo', 'criador', 'figurante', 'trazador', 'juez', 'inspector', 'faltaPago', 'fechaBaja', 'baja', 'motivoBajaUsuario']
        widgets = {
            'biografia': forms.Textarea(attrs={'class': 'form-control mt-3', 'rows': 5, 'placeholder': 'Biografia'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Direccion'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Telefono'}),
            'avatar': forms.ClearableFileInput(attrs={'class': 'form-control-file mt-3'}),
            'dni': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'DNI'}),
            'numeroSocio': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'NumeroSocio'}),
            'fechaNacimiento': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'fechaBaja': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'cuentaBancaria': forms.TextInput(attrs={'class': 'form-control mt-3', 'placeholder': 'Cuenta Bancaria'}),
            'baja': forms.CheckboxInput(attrs={'class':'form-check-input'}),

        }
        labels = {
            'biografia': 'Biografia',
            'direccion': 'Direccion',
            'telefono': 'Telefono',
            'avatar': 'Avatar',
            'dni': 'DNI',
            'numeroSocio': 'NumeroSocio',
            'fechaNacimiento': 'Fecha de Nacimiento',
            'baja': 'Baja',
        }



class EmailForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text="Requerido, 254 caracteres como máximo y debe ser válido")

    class Meta:
        model = User
        fields = ['email']
        
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if 'email' in self.changed_data:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError("El email introducido ya existe, introduzca uno diferente.")
        return email


