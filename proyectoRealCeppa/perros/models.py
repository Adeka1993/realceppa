from email.policy import default
from django.db import models
from ckeditor.fields import RichTextField
from general.models import Literal, FormaPago
from registration.models import User
from perfiles.models import Afijo, Pais, Region, Provincia



def custom_upload_to_HDRadioImg1(instance, filename):
    old_instance = HDRadio.objects.get(pk=instance.pk)
    old_instance.imagen1.delete()
    return 'HDRadio/'+filename


def custom_upload_to_HDRadioImg2(instance, filename):
    old_instance = HDRadio.objects.get(pk=instance.pk)
    old_instance.imagen2.delete()
    return 'HDRadio/'+filename    


def custom_upload_to_EDRadioImg1(instance, filename):
    old_instance = EDRadio.objects.get(pk=instance.pk)
    old_instance.imagen1.delete()
    return 'EDRadio/'+filename


def custom_upload_to_EDRadioImg2(instance, filename):
    old_instance = EDRadio.objects.get(pk=instance.pk)
    old_instance.imagen2.delete()
    return 'HEDRadio/'+filename  





#MODELOS   


#Revisado     
class MotivoBajaPerro(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Motivo Baja Perro"
        verbose_name_plural = "Motivos Bajas Perro"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class TipoCPR(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Tipo CPR"
        verbose_name_plural = "Tipos CPR"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion
   
#Revisado
class EstadoCPR(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Estado CPR"
        verbose_name_plural = "Estados CPR"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion  


#Revisado
class SexoPerro(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Sexo Perro"
        verbose_name_plural = "Sexos Perro"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class TipoPelo(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Tipo Pelo"
        verbose_name_plural = "Tipos Pelos"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class ColorMarcas(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Color Marcas"
        verbose_name_plural = "Colores Marcas"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion



#Revisado     
class MotivoBajaVeterinario(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Motivo Baja Veterinario"
        verbose_name_plural = "Motivos Bajas Veterinario"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado 
class Veterinario(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=200, null=True, blank=True)
    numColegiado = models.CharField(verbose_name="Numero Colegiado", max_length=200, null=True, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    codigoPostal = models.CharField(verbose_name="Código Postal", max_length=10, null=True, blank=True)
    poblacion = models.CharField(verbose_name="Población", max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", null=True, blank=True, on_delete=models.PROTECT,  related_name='Provincia_Veterinario_set')
    region = models.ForeignKey(Region, verbose_name="Región", null=True, blank=True, on_delete=models.PROTECT,  related_name='Region_Veterinario_set')
    pais = models.ForeignKey(Pais, verbose_name="Pais", null=True, blank=True, on_delete=models.PROTECT,  related_name='Pais_Veterinario_set')
    email = models.CharField(verbose_name="Email", max_length=100, null=True, blank=True)
    telefono = models.CharField(verbose_name="Teléfono", max_length=30, null=True, blank=True) 
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    motivoBajaVeterinario = models.ForeignKey(MotivoBajaVeterinario, verbose_name="Motivo Baja Veterinario", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_Veterinario_set')
    

    class Meta:
        verbose_name = "Veterinario"
        verbose_name_plural = "Veterinarios"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado  
class HDRadio(models.Model):
    fechaPrueba = models.DateTimeField(verbose_name="Fecha Prueba", null=True, blank=True)
    fechaResultado = models.DateTimeField(verbose_name="Fecha Resultado", null=True, blank=True)
    resultado = models.ForeignKey('HDResultado', verbose_name="HD Resultado", null=True, blank=True, on_delete=models.PROTECT,  related_name='HResultado_HDRadio_set')
    veterinario = models.ForeignKey(Veterinario, verbose_name="Veterinario", null=True, blank=True, on_delete=models.PROTECT,  related_name='Veterinario_HDRadio_set')
    imagen1 = models.ImageField(verbose_name="Imagen 1", upload_to=custom_upload_to_HDRadioImg1, null=True, blank=True)
    imagen2 = models.ImageField(verbose_name="Imagen 2", upload_to=custom_upload_to_HDRadioImg2, null=True, blank=True)

    class Meta:
        verbose_name = "HD Radio"
        verbose_name_plural = "HD Radio"
        ordering = ['fechaPrueba',]

    def __str__(self):
        return self.resultado.descripcion


#Revisado  
class HDResultado(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    
    class Meta:
        verbose_name = "HD Resultado"
        verbose_name_plural = "HD Resultados"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion



#Revisado  
class EDRadio(models.Model):
    fechaPrueba = models.DateTimeField(verbose_name="Fecha Prueba", null=True, blank=True)
    fechaResultado = models.DateTimeField(verbose_name="Fecha Resultado", null=True, blank=True)
    resultado = models.ForeignKey('EDResultado', verbose_name="ED Resultado", null=True, blank=True, on_delete=models.PROTECT,  related_name='EResultado_EDRadio_set')
    veterinario = models.ForeignKey(Veterinario, verbose_name="Veterinario", null=True, blank=True, on_delete=models.PROTECT,  related_name='Veterinario_EDRadio_set')
    imagen1 = models.ImageField(verbose_name="Imagen 1", upload_to=custom_upload_to_EDRadioImg1, null=True, blank=True)
    imagen2 = models.ImageField(verbose_name="Imagen 2", upload_to=custom_upload_to_EDRadioImg2, null=True, blank=True)

    class Meta:
        verbose_name = "ED Radio"
        verbose_name_plural = "ED Radio"
        ordering = ['fechaPrueba',]

    def __str__(self):
        return self.resultado.descripcion


#Revisado          
class EDResultado(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "ED Resultado"
        verbose_name_plural = "ED Resultados"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado  
class ADNResultado(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    literales = models.ManyToManyField(Literal, verbose_name="Literales")

    class Meta:
        verbose_name = "ADN Resultado"
        verbose_name_plural = "ADN Resultados"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion

#Revisado  
class Perro(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    lo = models.ForeignKey('LOPerro', verbose_name="Libro Origenes", null=True, blank=True, on_delete=models.PROTECT,  related_name='LO_Perro_set')
    nlo = models.CharField(verbose_name="NLO", max_length=50, null=True, blank=True)
    tatuaje = models.CharField(verbose_name="Tatuaje", max_length=50, null=True, blank=True)
    chip = models.CharField(verbose_name="Chip", max_length=50, null=True, blank=True)
    sexo = models.ForeignKey(SexoPerro, verbose_name="Sexo Perro", null=True, blank=True, on_delete=models.PROTECT,  related_name='Sexo_Perro_set')
    fechaNacimiento = models.DateTimeField(verbose_name="Fecha Nacimiento", null=True, blank=True)
    estadoPerro = models.ForeignKey('EstadoPerro', verbose_name="Estado Perro", null=True, blank=True, on_delete=models.PROTECT,  related_name='EstadoPerro_Perro_set')
    tipoPelo = models.ForeignKey('TipoPelo', verbose_name="Tipo Pelo", null=True, blank=True, on_delete=models.PROTECT,  related_name='TipoPelo_Perro_set')
    colorMarcas = models.ForeignKey('ColorMarcas', verbose_name="Color Marcas", null=True, blank=True, on_delete=models.PROTECT,  related_name='ColorMarcas_Perro_set')
    afijo = models.ForeignKey(Afijo, verbose_name="Afijo", null=True, blank=True, on_delete=models.PROTECT,  related_name='Afijo_Perro_set')
    origenLibrosExt = models.BooleanField(verbose_name="Origen Libros Ext.", null=True, blank=True)
    tipoCPR = models.ForeignKey('TipoCPR', verbose_name="Tipo CPR", null=True, blank=True, on_delete=models.PROTECT,  related_name='TipoCPR_Perro_set')
    estadoCPR = models.ForeignKey('EstadoCPR', verbose_name="Estado CPR", null=True, blank=True, on_delete=models.PROTECT,  related_name='EstadoCPR_Perro_set')
    fechaAptitudCria = models.DateTimeField(verbose_name="Fecha Aptitud Cría", null=True, blank=True)
    fechaSeleccionCria = models.DateTimeField(verbose_name="Fecha Selección Cría", null=True, blank=True)
    fechaBasicoCria = models.DateTimeField(verbose_name="Fecha Básico Cría", null=True, blank=True)
    padre = models.ForeignKey('Perro', verbose_name="Padre", null=True, blank=True, on_delete=models.PROTECT,  related_name='Padre_Perro_set')
    madre = models.ForeignKey('Perro', verbose_name="Madre", null=True, blank=True, on_delete=models.PROTECT,  related_name='Madre_Perro_set')
    camada = models.ForeignKey('Camada', verbose_name="Camada", null=True, blank=True, on_delete=models.PROTECT,  related_name='Camada_Perro_set')
    hdRadio = models.ForeignKey(HDRadio, verbose_name="HD Radio", null=True, blank=True, on_delete=models.PROTECT,  related_name='HDRadio_Perro_set')
    edRadio = models.ForeignKey(EDRadio, verbose_name="ED Radio", null=True, blank=True, on_delete=models.PROTECT,  related_name='EDRadio_Perro_set')
    adn = models.OneToOneField('ADNPerro', verbose_name="ADN", null=True, blank=True, on_delete=models.PROTECT,  related_name='ADN_Perro_set')
    korungTipo = models.ForeignKey('KorungTipo', verbose_name="Korung Tipo", null=True, blank=True, on_delete=models.PROTECT,  related_name='KorungTipo_Perro_set')
    korungAnys = models.CharField(verbose_name="Korung Anys", max_length=50, null=True, blank=True) 
    korungInforme = RichTextField(verbose_name="Korung Informe", blank=True, null=True)
    zb = models.CharField(verbose_name="ZB", max_length=10, null=True, blank=True) 
    fechaHabCamadaOcasional = models.DateTimeField(verbose_name="Fecha Hab. Camada Ocasional", null=True, blank=True)
    observaciones = RichTextField(verbose_name="Observaciones", blank=True, null=True)
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    motivoBajaPerro = models.ForeignKey('MotivoBajaPerro', verbose_name="Motivo Baja Perro", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_Perro_set') 

    class Meta:
        verbose_name = "Perro"
        verbose_name_plural = "Perros"
        ordering = ['fechaAlta', 'nombre']

    def __str__(self):
        return self.nombre



class EstadoPerro(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Estado Perro"
        verbose_name_plural = "Estados Perros"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisdo
class Prueba(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    mostrarEnPedigree = models.BooleanField(verbose_name="Mostrar En Pedigree")
    class Meta:
        verbose_name = "Prueba"
        verbose_name_plural = "Pruebas"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisdo
class PruebaPerro(models.Model):
    prueba = models.ForeignKey('Prueba', verbose_name="Prueba", null=True, blank=True, on_delete=models.PROTECT,  related_name='Prueba_PruebaPerro_set')
    perro = models.ForeignKey('Perro', verbose_name="Perro", null=True, blank=True, on_delete=models.PROTECT,  related_name='Perro_PruebaPerro_set')
    nivel = models.SmallIntegerField(verbose_name="Nivel", default=0)
    fechaPrueba = models.DateTimeField(verbose_name="Fecha Prueba")

    class Meta:
        verbose_name = "Prueba Perro"
        verbose_name_plural = "Pruebas Perros"
        ordering = ['fechaPrueba',]

    def __str__(self):
        return self.descripcion



#Revisdo
class KorungTipo(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Korung Tipo"
        verbose_name_plural = "Korung Tipos"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisdo
class LOPerro(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Libro Origenes Perro"
        verbose_name_plural = "Libro Origenes Perros"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class Titular(models.Model):
    titular = models.ForeignKey(User, verbose_name="Titular", on_delete=models.PROTECT, null=True, blank=True, related_name='Titular_Titulares_set')
    perro_titular = models.ForeignKey(Perro, verbose_name="Perro", on_delete=models.PROTECT,null=True, blank=True,  related_name='Perro_Titulares_set')
    fechaInicio = models.DateTimeField(verbose_name="Fecha Inicio", null=True, blank=True)
    fechaFin = models.DateTimeField(verbose_name="Fecha Fin", null=True, blank=True)
    class Meta:
        verbose_name = "Titular"
        verbose_name_plural = "Titulares"
        ordering = ['titular__username',]

#Revisado
class Cesionario(models.Model):
    cesionario = models.ForeignKey(User, verbose_name="Cesionario", on_delete=models.PROTECT,null=True, blank=True,  related_name='Cesionario_Cesionarios_set')
    perro_cesionario = models.ForeignKey(Perro, verbose_name="Perro", on_delete=models.PROTECT,null=True, blank=True,  related_name='Perro_Cesionarios_set')
    fechaInicio = models.DateTimeField(verbose_name="Fecha Inicio", null=True, blank=True)
    fechaFin = models.DateTimeField(verbose_name="Fecha Fin", null=True, blank=True)
    class Meta:
        verbose_name = "Cesionario"
        verbose_name_plural = "Cesionarios"
        ordering = ['cesionario__username',]


#Revisado
class EstadoADN(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Estado ADN"
        verbose_name_plural = "Estados ADN"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class ADNPerro(models.Model):
    fechaExtraccion = models.DateTimeField(verbose_name="Fecha Estracción", null=True, blank=True)
    SZNr = models.CharField(verbose_name="SZNr", max_length=50, null=True, blank=True)
    verb = models.CharField(verbose_name="verb", max_length=1, null=True, blank=True)
    estadoADN = models.ForeignKey(EstadoADN, verbose_name="Estado ADN", null=True, blank=True, on_delete=models.PROTECT,  related_name='EstadoADN_ADN_set')
    fechaLager = models.DateTimeField(verbose_name="Fecha Lager", null=True, blank=True) 
    largerNR = models.CharField(verbose_name="largerNR", max_length=50, null=True, blank=True)
    fechaBalance = models.DateTimeField(verbose_name="Fecha Balance", null=True, blank=True) 
    ADNResultado = models.ForeignKey(ADNResultado, verbose_name="ADN Resultado", null=True, blank=True, on_delete=models.PROTECT,  related_name='ADNResultado_ADN_set')

    class Meta:
        verbose_name = "ADN Perro"
        verbose_name_plural = "ADN Perros"
        ordering = ['SZNr',]

    def __str__(self):
        return self.SZNr



#Revisado
class PeticionSalto(models.Model):
    numDocumentoPeticion = models.CharField(verbose_name="Nº Documento Petición", max_length=100)
    socio = models.ForeignKey(User, verbose_name="Socio", null=True, blank=True, on_delete=models.PROTECT,  related_name='Socio_PeticionSalto_set')
    fechaPeticion = models.DateTimeField(verbose_name="Fecha Petición", null=True, blank=True)
    pagado = models.BooleanField(verbose_name="Pagado", null=True, blank=True)
    fechaPago = models.DateTimeField(verbose_name="Fecha Pago", null=True, blank=True)
    enviado = models.BooleanField(verbose_name="Enviado", null=True, blank=True)
    fechaEnvio = models.DateTimeField(verbose_name="Fecha Envío", null=True, blank=True)
    numFactura = models.CharField(verbose_name="Nº Factura", max_length=50, null=True, blank=True)
    formaPago = models.ForeignKey(FormaPago, verbose_name="Forma Pago", null=True, blank=True, on_delete=models.PROTECT,  related_name='FormaPago_PeticionSalto_set')
    
    class Meta:
        verbose_name = "Petición Salto"
        verbose_name_plural = "Peticiones Salto"
        ordering = ['fechaPeticion',]

    def __str__(self):
        return self.numDocumentoPeticion


#Revisado
class Salto(models.Model):
    peticionSalto = models.ForeignKey(PeticionSalto, verbose_name="Peticion Salto", null=True, blank=True, on_delete=models.PROTECT,  related_name='PeticionSalto_Salto_set')
    validacion = models.ForeignKey('ValidacionSalto', verbose_name="Validación", null=True, blank=True, on_delete=models.PROTECT,  related_name='Validacion_Salto_set')
    socio = models.ForeignKey(User, verbose_name="Socio", null=True, blank=True, on_delete=models.PROTECT,  related_name='Socio_Salto_set')
    fechaSalto = models.DateTimeField(verbose_name="Fecha Salto", null=True, blank=True)
    fechaComunicacion = models.DateTimeField(verbose_name="Fecha Comunicación", null=True, blank=True)
    hembra = models.ForeignKey(Perro, verbose_name="Hembra", null=True, blank=True, on_delete=models.PROTECT,  related_name='Hembra_Salto_set')
    macho = models.ForeignKey(Perro, verbose_name="Macho", null=True, blank=True, on_delete=models.PROTECT,  related_name='Macho_Salto_set')
    afijo = models.ForeignKey(Afijo, verbose_name="Afijo", null=True, blank=True, on_delete=models.PROTECT,  related_name='Afijo_Salto_set')

    class Meta:
        verbose_name = "Salto"
        verbose_name_plural = "Saltos"
        ordering = ['peticionSalto__numDocumentoPeticion',]



#Revisado
class ValidacionSalto(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Validación Salto"
        verbose_name_plural = "Validaciones Salto"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class Camada(models.Model):
    salto = models.ForeignKey(Salto, verbose_name="Salto", null=True, blank=True, on_delete=models.PROTECT,  related_name='Salto_Camada_set')
    fechaCamada = models.DateTimeField(verbose_name="Fecha Camada", null=True, blank=True)
    fechaComunicacion = models.DateTimeField(verbose_name="Fecha Comunicación", null=True, blank=True)
    afijo = models.ForeignKey(Afijo, verbose_name="Afijo", null=True, blank=True, on_delete=models.PROTECT,  related_name='Afijo_Camada_set')
    criador = models.ForeignKey(User, verbose_name="Criador", null=True, blank=True, on_delete=models.PROTECT,  related_name='Criador_Camada_set')
    NHTotales = models.SmallIntegerField(verbose_name="NH Totales", default=0, null=True, blank=True)
    NMTotales = models.SmallIntegerField(verbose_name="NM Totales", default=0, null=True, blank=True)
    NHNacidosMuertos = models.SmallIntegerField(verbose_name="NH Nacidos Muertos", default=0, null=True, blank=True)
    NMNacidosMuertos = models.SmallIntegerField(verbose_name="NM Nacidos Muertos", default=0, null=True, blank=True)
    NHMuertosPost = models.SmallIntegerField(verbose_name="NH Muertos Post", default=0, null=True, blank=True)
    NMMuertosPost = models.SmallIntegerField(verbose_name="NM Muertos Post", default=0, null=True, blank=True)
    NHInsCPR = models.SmallIntegerField(verbose_name="NH Ins CPR", default=0, null=True, blank=True)
    NMInsCPR = models.SmallIntegerField(verbose_name="NM Ins CPR", default=0, null=True, blank=True)
    NHVarCompr = models.SmallIntegerField(verbose_name="NH Var Compr", default=0, null=True, blank=True)
    NMVarCompr = models.SmallIntegerField(verbose_name="NM Var Compr", default=0, null=True, blank=True)
    fechaInspeccion = models.DateTimeField(verbose_name="Fecha Inspección", null=True, blank=True)
    buenEstadoMadre = models.BooleanField(verbose_name="Buen Estado Madre", null=True, blank=True)
    BEMIncidencias = RichTextField(verbose_name="BEM Incidencias",  null=True, blank=True)
    buenEstadoCachorros = models.BooleanField(verbose_name="Buen Estado Cachorros", null=True, blank=True)
    BECIncidencias = RichTextField(verbose_name="BEC Incidencias",  null=True, blank=True)
    observaciones = RichTextField(verbose_name="Observaciones",  null=True, blank=True)
    fechaEnvioEmailDelegacion = models.DateTimeField(verbose_name="Fecha Envío Email Delegación", null=True, blank=True)

    class Meta:
        verbose_name = "Camada"
        verbose_name_plural = "Camadas"
        ordering = ['-fechaCamada',]



#Revisado
class ZBClase(models.Model):
    descripcionCorta = models.CharField(verbose_name="Descripción Corta", max_length=200)
    literalesDescCorta = models.ManyToManyField(Literal,verbose_name="Literales Desc. Corta")
    descripcion = RichTextField(verbose_name="Descripción", null=True, blank=True)
    mesesIniciales = models.IntegerField(verbose_name="Meses Iniciales", null=True, blank=True)
    mesesFinales = models.IntegerField(verbose_name="Meses Finales", null=True, blank=True)

    class Meta:
        verbose_name = "ZB Clase"
        verbose_name_plural = "ZB Clases"
        ordering = ['descripcionCorta',]

    def __str__(self):
        return self.descripcionCorta


#Revisado
class ZBResultado(models.Model):
    abreviatura = models.CharField(verbose_name="Abreviatura", max_length=10)
    claseZB = models.ForeignKey(User, verbose_name="Clase ZB", null=True, blank=True, on_delete=models.PROTECT,  related_name='ClaseZB_ZBResultado_set')
    descripcion = models.CharField(verbose_name="Descripción", max_length=200, null=True, blank=True)
    orden = models.IntegerField(verbose_name="Orden", null=True, blank=True)

    class Meta:
        verbose_name = "ZB Resultado"
        verbose_name_plural = "ZB Resultados"
        ordering = ['abreviatura',]

    def __str__(self):
        return self.abreviatura


#Revisado
class EstadoDentadura(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")

    class Meta:
        verbose_name = "Estado Dentadura"
        verbose_name_plural = "Estados Dentadura"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion

#Revisado
class Dentadura(models.Model):
    perro = models.OneToOneField(Perro, on_delete=models.CASCADE, related_name='Perro_Dentadura_set')
    fechaPrueba = models.DateTimeField(verbose_name="Fecha Prueba", null=True, blank=True)
    lugarPrueba = models.CharField(verbose_name="Lugar Prueba", max_length=200, null=True, blank=True)
    juez = models.ForeignKey(User, verbose_name="Juez", null=True, blank=True, on_delete=models.PROTECT,  related_name='Juez_Dentadura_set')
    
    
    SupIzqIncisivo1Presente = models.BooleanField(verbose_name="Sup. Izq. Incisivo 1 Presente", null=True, blank=True)
    SupIzqIncisivo1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Incisivo 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqIncisivo1Estado_Dentadura_set')
    SupIzqIncisivo2Presente = models.BooleanField(verbose_name="Sup. Izq. Incisivo 2 Presente", null=True, blank=True)
    SupIzqIncisivo2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Incisivo 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqIncisivo2Estado_Dentadura_set')
    SupIzqIncisivo3Presente = models.BooleanField(verbose_name="Sup. Izq. Incisivo 3 Presente", null=True, blank=True)
    SupIzqIncisivo3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Incisivo 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqIncisivo3Estado_Dentadura_set')
    SupIzqCaninoPresente = models.BooleanField(verbose_name="Sup. Izq. Canino Presente", null=True, blank=True)
    SupIzqCaninoEstado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Canino Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqCaninoEstado_Dentadura_set')
    SupIzqPremolar1Presente = models.BooleanField(verbose_name="Sup. Izq. Premolar 1 Presente", null=True, blank=True)
    SupIzqPremolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Premolar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqPremolar1Estado_Dentadura_set')
    SupIzqPremolar2Presente = models.BooleanField(verbose_name="Sup. Izq. Premolar 2 Presente", null=True, blank=True)
    SupIzqPremolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Premolar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqPremolar2Estado_Dentadura_set')
    SupIzqPremolar3Presente = models.BooleanField(verbose_name="Sup. Izq. Premolaboolr 3 Presente", null=True, blank=True)
    SupIzqPremolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Premolar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqPremolar3Estado_Dentadura_set')
    SupIzqPremolar4Presente = models.BooleanField(verbose_name="Sup. Izq. Premolar 4 Presente", null=True, blank=True)
    SupIzqPremolar4Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Premolar 4 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqPremolar4Estado_Dentadura_set')
    SupIzqMolar1Presente = models.BooleanField(verbose_name="Sup. Izq. Molar 1 Presente", null=True, blank=True)
    SupIzqMolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Molar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqMolar1Estado_Dentadura_set')
    SupIzqMolar2Presente = models.BooleanField(verbose_name="Sup. Izq. Molar 2 Presente", null=True, blank=True)
    SupIzqMolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Izq. Molar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupIzqMolar2Estado_Dentadura_set')
    


    SupDerIncisivo1Presente = models.BooleanField(verbose_name="Sup. Der. Incisivo 1 Presente", null=True, blank=True)
    SupDerIncisivo1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Incisivo 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerIncisivo1Estado_Dentadura_set')
    SupDerIncisivo2Presente = models.BooleanField(verbose_name="Sup. Der. Incisivo 2 Presente", null=True, blank=True)
    SupDerIncisivo2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Incisivo 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerIncisivo2Estado_Dentadura_set')
    SupDerIncisivo3Presente = models.BooleanField(verbose_name="Sup. Der. Incisivo 3 Presente", null=True, blank=True)
    SupDerIncisivo3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Incisivo 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerIncisivo3Estado_Dentadura_set')
    SupDerCaninoPresente = models.BooleanField(verbose_name="Sup. Der. Canino Presente", null=True, blank=True)
    SupDerCaninoEstado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Canino Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerCaninoEstado_Dentadura_set')
    SupDerPremolar1Presente = models.BooleanField(verbose_name="Sup. Der. Premolar 1 Presente", null=True, blank=True)
    SupDerPremolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Premolar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerPremolar1Estado_Dentadura_set')
    SupDerPremolar2Presente = models.BooleanField(verbose_name="Sup. Der. Premolar 2 Presente", null=True, blank=True)
    SupDerPremolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Premolar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerPremolar2Estado_Dentadura_set')
    SupDerPremolar3Presente = models.BooleanField(verbose_name="Sup. Der. Premolar 3 Presente", null=True, blank=True)
    SupDerPremolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Premolar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerPremolar3Estado_Dentadura_set')
    SupDerPremolar4Presente = models.BooleanField(verbose_name="Sup. Der. Premolar 4 Presente", null=True, blank=True)
    SupDerPremolar4Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Premolar 4 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerPremolar4Estado_Dentadura_set')
    SupDerMolar1Presente = models.BooleanField(verbose_name="Sup. Der. Molar 1 Presente", null=True, blank=True)
    SupDerMolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Molar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerMolar1Estado_Dentadura_set')
    SupDerMolar2Presente = models.BooleanField(verbose_name="Sup. Der. Molar 2 Presente", null=True, blank=True)
    SupDerMolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Sup. Der. Molar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='SupDerMolar2Estado_Dentadura_set')
    


    InfIzqIncisivo1Presente = models.BooleanField(verbose_name="Inf. Izq. Incisivo 1 Presente", null=True, blank=True)
    InfIzqIncisivo1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Incisivo 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqIncisivo1Estado_Dentadura_set')
    InfIzqIncisivo2Presente = models.BooleanField(verbose_name="Inf. Izq. Incisivo 2 Presente", null=True, blank=True)
    InfIzqIncisivo2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Incisivo 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqIncisivo2Estado_Dentadura_set')
    InfIzqIncisivo3Presente = models.BooleanField(verbose_name="Inf. Izq. Incisivo 3 Presente", null=True, blank=True)
    InfIzqIncisivo3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Incisivo 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqIncisivo3Estado_Dentadura_set')
    InfIzqCaninoPresente = models.BooleanField(verbose_name="Inf. Izq. Canino Presente", null=True, blank=True)
    InfIzqCaninoEstado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Canino Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqCaninoEstado_Dentadura_set')
    InfIzqPremolar1Presente = models.BooleanField(verbose_name="Inf. Izq. Premolar 1 Presente", null=True, blank=True)
    InfIzqPremolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Premolar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqPremolar1Estado_Dentadura_set')
    InfIzqPremolar2Presente = models.BooleanField(verbose_name="Inf. Izq. Premolar 2 Presente", null=True, blank=True)
    InfIzqPremolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Premolar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqPremolar2Estado_Dentadura_set')
    InfIzqPremolar3Presente = models.BooleanField(verbose_name="Inf. Izq. Premolaboolr 3 Presente", null=True, blank=True)
    InfIzqPremolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Premolar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqPremolar3Estado_Dentadura_set')
    InfIzqPremolar4Presente = models.BooleanField(verbose_name="Inf. Izq. Premolar 4 Presente", null=True, blank=True)
    InfIzqPremolar4Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Premolar 4 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqPremolar4Estado_Dentadura_set')
    InfIzqMolar1Presente = models.BooleanField(verbose_name="Inf. Izq. Molar 1 Presente", null=True, blank=True)
    InfIzqMolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Molar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqMolar1Estado_Dentadura_set')
    InfIzqMolar2Presente = models.BooleanField(verbose_name="Inf. Izq. Molar 2 Presente", null=True, blank=True)
    InfIzqMolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Molar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqMolar2Estado_Dentadura_set')
    InfIzqMolar3Presente = models.BooleanField(verbose_name="Inf. Izq. Molar 3 Presente", null=True, blank=True)
    InfIzqMolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Izq. Molar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfIzqMolar3Estado_Dentadura_set')
    


    InfDerIncisivo1Presente = models.BooleanField(verbose_name="Inf. Der. Incisivo 1 Presente", null=True, blank=True)
    InfDerIncisivo1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Incisivo 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerIncisivo1Estado_Dentadura_set')
    InfDerIncisivo2Presente = models.BooleanField(verbose_name="Inf. Der. Incisivo 2 Presente", null=True, blank=True)
    InfDerIncisivo2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Incisivo 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerIncisivo2Estado_Dentadura_set')
    InfDerIncisivo3Presente = models.BooleanField(verbose_name="Inf. Der. Incisivo 3 Presente", null=True, blank=True)
    InfDerIncisivo3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Incisivo 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerIncisivo3Estado_Dentadura_set')
    InfDerCaninoPresente = models.BooleanField(verbose_name="Inf. Der. Canino Presente", null=True, blank=True)
    InfDerCaninoEstado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Canino Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerCaninoEstado_Dentadura_set')
    InfDerPremolar1Presente = models.BooleanField(verbose_name="Inf. Der. Premolar 1 Presente", null=True, blank=True)
    InfDerPremolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Premolar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerPremolar1Estado_Dentadura_set')
    InfDerPremolar2Presente = models.BooleanField(verbose_name="Inf. Der. Premolar 2 Presente", null=True, blank=True)
    InfDerPremolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Premolar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerPremolar2Estado_Dentadura_set')
    InfDerPremolar3Presente = models.BooleanField(verbose_name="Inf. Der. Premolar 3 Presente", null=True, blank=True)
    InfDerPremolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Premolar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerPremolar3Estado_Dentadura_set')
    InfDerPremolar4Presente = models.BooleanField(verbose_name="Inf. Der. Premolar 4 Presente", null=True, blank=True)
    InfDerPremolar4Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Premolar 4 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerPremolar4Estado_Dentadura_set')
    InfDerMolar1Presente = models.BooleanField(verbose_name="Inf. Der. Molar 1 Presente", null=True, blank=True)
    InfDerMolar1Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Molar 1 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerMolar1Estado_Dentadura_set')
    InfDerMolar2Presente = models.BooleanField(verbose_name="Inf. Der. Molar 2 Presente", null=True, blank=True)
    InfDerMolar2Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Molar 2 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerMolar2Estado_Dentadura_set')
    InfDerMolar3Presente = models.BooleanField(verbose_name="Inf. Der. Molar 3 Presente", null=True, blank=True)
    InfDerMolar3Estado = models.ForeignKey(EstadoDentadura, verbose_name="Inf. Der. Molar 3 Estado", null=True, blank=True, on_delete=models.PROTECT,  related_name='InfDerMolar3Estado_Dentadura_set')
    

    class Meta:
        verbose_name = "Dentadura"
        verbose_name_plural = "Dentaduras"
        ordering = ['fechaPrueba',]


