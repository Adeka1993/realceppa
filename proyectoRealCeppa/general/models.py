from django.db import models


# Create your models here.

#Revisado  
class Idioma(models.Model):
    codigoIdioma = models.CharField(verbose_name="Código Idioma", max_length=2, unique=True)
    idioma = models.CharField(verbose_name="Idioma", max_length=50, unique=True)
    class Meta:
        verbose_name = "Idioma"
        verbose_name_plural = "Idiomas"
        ordering = ['idioma',]

    def __str__(self):
        return self.idioma

#Revisado  
class Literal(models.Model):
    literal = models.CharField(verbose_name="Literal", max_length=255)
    idioma = models.ForeignKey(Idioma, verbose_name="Idioma", on_delete=models.PROTECT,  related_name='Idioma_Literal_set')
    class Meta:
        verbose_name = "Literal"
        verbose_name_plural = "Literales"
        ordering = ['literal',]

    def __str__(self):
        return self.literal


#Revisado                  
class Tratamiento(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=200)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Tratamiento"
        verbose_name_plural = "Tratamientos"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion


#Revisado  
class Pais(models.Model):
    nombre = models.CharField(verbose_name="Nombre País", max_length=200, unique=True)
    codigo = models.CharField(verbose_name="Código país", max_length=2, unique=True)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "País"
        verbose_name_plural = "Países"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado 
class Region(models.Model):
    nombre = models.CharField(verbose_name="Nombre Región", max_length=200)
    pais = models.ForeignKey(Pais, verbose_name="País", null=True, blank=True, on_delete=models.PROTECT,  related_name='Pais_Region_set')
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Región"
        verbose_name_plural = "Regiones"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado
class Provincia(models.Model):
    nombre = models.CharField(verbose_name="Nombre Provincia", max_length=100)
    region = models.ForeignKey(Region, verbose_name="Región", null=True, blank=True, on_delete=models.PROTECT,  related_name='Region_Provincia_set')
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Provincia"
        verbose_name_plural = "Provincias"
        ordering = ['nombre',]

    def __str__(self):
        return self.nombre


#Revisado
class FormaPago(models.Model):
    descripcion = models.CharField(verbose_name="Descripción", max_length=100)
    literales = models.ManyToManyField(Literal,verbose_name="Literales")
    class Meta:
        verbose_name = "Forma Pago"
        verbose_name_plural = "Formas Pago"
        ordering = ['descripcion',]

    def __str__(self):
        return self.descripcion







                
