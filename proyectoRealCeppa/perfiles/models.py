from email.policy import default
from pickle import TRUE
from django.db import models
from registration.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from general.models import Literal, Tratamiento, Pais, Region, Provincia



@receiver(post_save, sender = User)
def ensure_rpofile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Perfil.objects.get_or_create(user=instance)


def custom_upload_to(instance, filename):
    old_instance = Perfil.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'perfiles/'+filename


#MODELOS

#Revisado
class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='Usuario_Perfil_set')
    avatar = models.ImageField(verbose_name="Avatar", upload_to=custom_upload_to, null=True, blank=True)
    biografia = models.TextField(verbose_name="Biografía",null=True, blank=True)
    dni = models.CharField(verbose_name="DNI", max_length=50, null=True, blank=True, unique=True)
    numeroSocio = models.CharField(verbose_name="Número socio", max_length=50,  null=True, blank=True)
    tipoSocio = models.ForeignKey('TipoSocio', verbose_name="Tipo Socio", null=True, blank=True, on_delete=models.PROTECT,  related_name='TipoSocio_Perfil_set')
    tratamiento =  models.ForeignKey(Tratamiento, verbose_name="Tratamiento", null=True, blank=True, on_delete=models.PROTECT,  related_name='Tratamiento_Perfil_set')
    fechaNacimiento = models.DateTimeField(verbose_name="Fecha Nacimiento", null=True, blank=True)
    direccion = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    codigoPostal = models.CharField(verbose_name="Código Postal", max_length=10, null=True, blank=True)
    poblacion = models.CharField(verbose_name="Población", max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", null=True, blank=True, on_delete=models.PROTECT,  related_name='Provincia_Perfil_set')
    region = models.ForeignKey(Region, verbose_name="Región", null=True, blank=True, on_delete=models.PROTECT,  related_name='Region_Perfil_set')
    pais = models.ForeignKey(Pais, verbose_name="Pais", null=True, blank=True, on_delete=models.PROTECT,  related_name='Pais_Perfil_set')
    email = models.CharField(verbose_name="Email", max_length=100, null=True, blank=True)
    telefono = models.CharField(verbose_name="Teléfono", max_length=30, null=True, blank=True)
    delegacion = models.ForeignKey('Delegacion', verbose_name="Delegación", null=True, blank=True, on_delete=models.PROTECT,  related_name='Delegacion_Perfil_set')
    grupoTrabajo = models.ForeignKey('GrupoTrabajo', verbose_name="Grupo Trabajo", null=True, blank=True, on_delete=models.PROTECT,  related_name='GrupoTrabajo_Perfil_set')
    afijo = models.ForeignKey('Afijo', verbose_name="Afijo", null=True, blank=True, on_delete=models.PROTECT,  related_name='Afijo_Perfil_set')
    criador = models.BooleanField(verbose_name="Criador", null=True, blank=True)
    figurante = models.BooleanField(verbose_name="Figurante", null=True, blank=True)
    trazador = models.BooleanField(verbose_name="Trazador", null=True, blank=True)
    juez = models.BooleanField(verbose_name="Juez", null=True, blank=True)
    inspector = models.BooleanField(verbose_name="Inspector", null=True, blank=True)
    faltaPago = models.BooleanField(verbose_name="Falta Pago", null=True, blank=True)
    cuentaBancaria = models.CharField(verbose_name="Cuenta Bancaria", max_length=30, null=True, blank=True)
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    motivoBajaUsuario = models.ForeignKey('MotivoBajaUsuario', verbose_name="Motivo Baja Usuario", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_Perfil_set')
    class Meta:
        verbose_name = "Perfil"
        verbose_name_plural = "Perfiles"
        ordering=['user__username']


#Revisado
class MotivoBajaUsuario(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Motivo Baja Usuario"
        verbose_name_plural = "Motivos Baja Usuario"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion



#Revisado       
class Delegacion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    direccion = models.CharField(verbose_name="Dirección", max_length=100, null=True, blank=True)
    codigoPostal = models.CharField(verbose_name="Código Postal", max_length=10, null=True, blank=True)
    poblacion = models.CharField(verbose_name="Población", max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", null=True, blank=True, on_delete=models.PROTECT,  related_name='Provincia_Delegacion_set')
    region = models.ForeignKey(Region, verbose_name="Región", null=True, blank=True, on_delete=models.PROTECT,  related_name='Region_Delegacion_set')
    pais = models.ForeignKey(Pais, verbose_name="Pais", null=True, blank=True, on_delete=models.PROTECT,  related_name='Pais_Delegacion_set')
    email = models.CharField(verbose_name="Email", max_length=100, null=True, blank=True)
    url = models.CharField(verbose_name="URL", max_length=300, null=True, blank=True)
    telefono = models.CharField(verbose_name="Teléfono", max_length=30, null=True, blank=True)
    vocalCria = models.ForeignKey(User, verbose_name="Vocal Cría", null=True, blank=True, on_delete=models.PROTECT,  related_name='VocalCria_Delegacion_set')
    vocalTrabajo = models.ForeignKey(User, verbose_name="Vocal Trabajo", null=True, blank=True, on_delete=models.PROTECT,  related_name='VocalTrabajo_Delegacion_set')
    vocalPresidente = models.ForeignKey(User, verbose_name="Vocal Presidente", null=True, blank=True, on_delete=models.PROTECT,  related_name='VocalPresidente_Delegacion_set')
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    motivoBajaDelegacion = models.ForeignKey('MotivoBajaDelegacion', verbose_name="Motivo Baja Delegacion", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_Delegacion_set')
   
    class Meta:
        verbose_name = "Delegación"
        verbose_name_plural = "Delegaciones"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado
class MotivoBajaDelegacion(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Motivo Baja Delegación"
        verbose_name_plural = "Motivos Baja Delegaciones"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion



#Revisado
class Afijo(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    motivoBajaAfijo = models.ForeignKey('MotivoBajaAfijo', verbose_name="Motivo Baja Afijo", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_Afijo_set')
   
    class Meta:
        verbose_name = "Afijo"
        verbose_name_plural = "Afijos"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado
class MotivoBajaAfijo(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Motivo Baja Afijo"
        verbose_name_plural = "Motivos Baja Afijo"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class GrupoTrabajo(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    direccion = models.CharField(verbose_name="Dirección", max_length=200, null=True, blank=True)
    codigoPostal = models.CharField(verbose_name="Código Postal", max_length=10, null=True, blank=True)
    poblacion = models.CharField(verbose_name="Población", max_length=100, null=True, blank=True)
    provincia = models.ForeignKey(Provincia, verbose_name="Provincia", null=True, blank=True, on_delete=models.PROTECT,  related_name='Provincia_GrupoTrabajo_set')
    region = models.ForeignKey(Region, verbose_name="Región", null=True, blank=True, on_delete=models.PROTECT,  related_name='Region_GrupoTrabajo_set')
    pais = models.ForeignKey(Pais, verbose_name="Pais", null=True, blank=True, on_delete=models.PROTECT,  related_name='Pais_GrupoTrabajo_set')
    delegacion = models.ForeignKey(Delegacion,verbose_name="Delegación", null=True, blank=True, on_delete=models.PROTECT,  related_name='Delegacion_GrupoTrabajo_set')
    telefono = models.CharField(verbose_name="Teléfono", max_length=30, null=True, blank=True)
    email = models.CharField(verbose_name="Email", max_length=100, null=True, blank=True)
    url = models.CharField(verbose_name="URL", max_length=300, null=True, blank=True)
    responsable = models.ForeignKey(User,verbose_name="Responsable", null=True, blank=True, on_delete=models.PROTECT,  related_name='Responsable_GrupoTrabajo_set')
    monitorInstructor = models.ForeignKey(User,verbose_name="Monitor/Instructor", null=True, blank=True, on_delete=models.PROTECT,  related_name='MonitorInstructor_GrupoTrabajo_set')
    diasEntrenamiento = models.IntegerField(verbose_name="Días Entrenamiento", null=True, blank=True)
    fechaAlta = models.DateTimeField(auto_now_add=True, verbose_name="Fecha Alta")
    fechaModificacion = models.DateTimeField(auto_now=True, verbose_name="Fecha Modificación")
    fechaBaja = models.DateTimeField(verbose_name="Fecha Baja", null=True, blank=True)
    baja = models.BooleanField(verbose_name="Baja", default=False, blank=True, null=True)
    motivoBajaGrupoTrabajo = models.ForeignKey('MotivoBajaGrupoTrabajo', verbose_name="Motivo Baja Grupo Trabajo", null=True, blank=True, on_delete=models.PROTECT,  related_name='MotivoBaja_GrupoTrabajo_set')
   
    
    class Meta:
        verbose_name = "Grupo Trabajo"
        verbose_name_plural = "Grupos Trabajo"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado
class MotivoBajaGrupoTrabajo(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Motivo Baja Grupo Trabajo"
        verbose_name_plural = "Motivos Baja Grupo Trabajo"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado
class TipoSocio(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Tipo Socio"
        verbose_name_plural = "Tipos Socios"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion