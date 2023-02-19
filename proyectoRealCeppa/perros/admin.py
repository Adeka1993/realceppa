from django.contrib import admin

from .models import  SexoPerro, HDResultado, EDResultado, ADNResultado,  Titular
from .models import TipoPelo, ColorMarcas, MotivoBajaPerro, TipoCPR, EstadoCPR, Cesionario, EstadoPerro
from .models import EstadoADN, ADNPerro, PeticionSalto, Salto, Camada, Perro, MotivoBajaVeterinario, Veterinario, HDRadio, EDRadio
from .models import KorungTipo, LOPerro, ValidacionSalto, ZBClase, ZBResultado, EstadoDentadura, Dentadura, Prueba, PruebaPerro


# Register your models here.


#Revisado
class MotivoBajaPerroAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([mbp.literal for mbp in obj.literales.all()])

admin.site.register(MotivoBajaPerro, MotivoBajaPerroAdmin)


#Revisado
class TipoCPRAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([tcpr.literal for tcpr in obj.literales.all()])

admin.site.register(TipoCPR, TipoCPRAdmin)


#Revisado
class EstadoPerroAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([tcpr.literal for tcpr in obj.literales.all()])

admin.site.register(EstadoPerro, EstadoPerroAdmin)

#Revisado
class EstadoCPRAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([ecpr.literal for ecpr in obj.literales.all()])

admin.site.register(EstadoCPR, EstadoCPRAdmin)



#Revisado
class SexoPerroAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
        
    def Lista_literales(self, obj):
        return "\n".join([sp.literal for sp in obj.literales.all()])

admin.site.register(SexoPerro, SexoPerroAdmin)


#Revisado
class TipoPeloAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([tp.literal for tp in obj.literales.all()])

admin.site.register(TipoPelo, TipoPeloAdmin)



#Revisado
class ColorMarcasAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([cm.literal for cm in obj.literales.all()])

admin.site.register(ColorMarcas, ColorMarcasAdmin)



#Revisado
class MotivoBajaVeterinarioAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([mbv.literal for mbv in obj.literales.all()])

admin.site.register(MotivoBajaVeterinario, MotivoBajaVeterinarioAdmin)


#Revisado
class PruebaAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales','mostrarEnPedigree')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([mbv.literal for mbv in obj.literales.all()])

admin.site.register(Prueba, PruebaAdmin)



#Revisado
class PruebaPerroAdmin(admin.ModelAdmin):
    list_display = ('prueba','perro', 'nivel','fechaPrueba')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(PruebaPerro, PruebaPerroAdmin)



#Revisado
class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ('nombre','numColegiado', 'email', 'telefono', 'provincia', 'region', 'pais', 'fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaVeterinario')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Veterinario, VeterinarioAdmin)


#Revisado
class HDRadioAdmin(admin.ModelAdmin):
    list_display = ('fechaPrueba', 'fechaResultado','resultado','veterinario')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(HDRadio, HDRadioAdmin)


#Revisado
class HDResultadoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([hdr.literal for hdr in obj.literales.all()])

admin.site.register(HDResultado, HDResultadoAdmin)



#Revisado
class EDRadioAdmin(admin.ModelAdmin):
    list_display = ('fechaPrueba', 'fechaResultado','resultado','veterinario')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(EDRadio, EDRadioAdmin)


#Revisado
class EDResultadoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([edr.literal for edr in obj.literales.all()])

admin.site.register(EDResultado, EDResultadoAdmin)



#Revisado
class ADNResultadoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([adnr.literal for adnr in obj.literales.all()])

admin.site.register(ADNResultado, ADNResultadoAdmin)



#Revisado
class PerroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nlo', 'chip', 'sexo', 'fechaNacimiento', 'fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaPerro' )

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Perro, PerroAdmin)



#Revisado
class KorungTipoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([kt.literal for kt in obj.literales.all()])


admin.site.register(KorungTipo, KorungTipoAdmin)



#Revisado
class LOPerroAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([lop.literal for lop in obj.literales.all()])


admin.site.register(LOPerro, LOPerroAdmin)



#Revisado
class TitularAdmin(admin.ModelAdmin):
    list_display = ('titular','perro_titular', 'fechaInicio', 'fechaFin')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Titular, TitularAdmin)



#Revisado
class CesionarioAdmin(admin.ModelAdmin):
    list_display = ('cesionario','perro_cesionario', 'fechaInicio', 'fechaFin')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Cesionario, CesionarioAdmin)



#Revisado
class EstadoADNAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([eadn.literal for eadn in obj.literales.all()])

admin.site.register(EstadoADN, EstadoADNAdmin)



#Revisado
class ADNPerroAdmin(admin.ModelAdmin):
    list_display = ('fechaExtraccion', 'SZNr', 'verb', 'estadoADN', 'fechaLager', 'largerNR', 'fechaBalance', 'ADNResultado')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(ADNPerro, ADNPerroAdmin)



#Revisado
class PeticionSaltoAdmin(admin.ModelAdmin):
    list_display = ('numDocumentoPeticion', 'socio', 'fechaPeticion', 'pagado', 'fechaPago', 'enviado', 'fechaEnvio', 'formaPago')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(PeticionSalto, PeticionSaltoAdmin)


#Revisado
class SaltoAdmin(admin.ModelAdmin):
    list_display = ('peticionSalto', 'validacion', 'socio', 'fechaSalto', 'fechaComunicacion' , 'hembra', 'macho', 'afijo')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Salto, SaltoAdmin)



#Revisado
class ValidacionSaltoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([vs.literal for vs in obj.literales.all()])

admin.site.register(ValidacionSalto, ValidacionSaltoAdmin)


#Revisado
class CamadaAdmin(admin.ModelAdmin):
    list_display = ('fechaCamada', 'fechaComunicacion', 'afijo', 'criador', 'fechaEnvioEmailDelegacion')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Camada, CamadaAdmin)




#Revisado
class ZBClaseAdmin(admin.ModelAdmin):
    list_display = ('descripcionCorta','DescripcionCorta_literales', 'mesesIniciales', 'mesesFinales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def DescripcionCorta_literales(self, obj):
        return "\n".join([zbc.literal for zbc in obj.literales.all()])

admin.site.register(ZBClase, ZBClaseAdmin)




#Revisado
class ZBResultadoAdmin(admin.ModelAdmin):
    list_display = ('abreviatura', 'claseZB', 'descripcion', 'orden')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(ZBResultado, ZBResultadoAdmin)



#Revisado
class EstadoDentaduraAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

    def Lista_literales(self, obj):
        return "\n".join([ed.literal for ed in obj.literales.all()])


admin.site.register(EstadoDentadura, EstadoDentaduraAdmin)





#Revisado
class DentaduraAdmin(admin.ModelAdmin):
    list_display = ('perro','fechaPrueba', 'lugarPrueba', 'juez')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }


admin.site.register(Dentadura, DentaduraAdmin)
