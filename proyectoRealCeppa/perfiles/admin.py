from django.contrib import admin
from .models import Afijo, Delegacion, Perfil, TipoSocio, MotivoBajaUsuario,MotivoBajaDelegacion,MotivoBajaAfijo, GrupoTrabajo, MotivoBajaGrupoTrabajo


#Revisado
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user','dni','numeroSocio','tipoSocio','email', 'telefono', 'provincia', 'region',
    'pais', 'fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaUsuario')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }

admin.site.register(Perfil, PerfilAdmin)


#Revisado
class MotivoBajaUsuarioAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([mbu.literal for mbu in obj.literales.all()])

admin.site.register(MotivoBajaUsuario, MotivoBajaUsuarioAdmin)


#Revisado
class DelegacionAdmin(admin.ModelAdmin):
    list_display = ('nombre','Lista_literales','email', 'telefono', 'vocalCria', 'vocalTrabajo', 'vocalPresidente',  'provincia', 'region',
    'pais', 'fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaDelegacion')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([dl.literal for dl in obj.literales.all()])


admin.site.register(Delegacion, DelegacionAdmin)


#Revisado
class MotivoBajaDelegacionAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([mbd.literal for mbd in obj.literales.all()])

admin.site.register(MotivoBajaDelegacion, MotivoBajaDelegacionAdmin)



#Revisado
class AfijoAdmin(admin.ModelAdmin):
    list_display = ('nombre','Lista_literales','fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaAfijo')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([af.literal for af in obj.literales.all()])

admin.site.register(Afijo, AfijoAdmin)



#Revisado
class MotivoBajaAfijoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([mba.literal for mba in obj.literales.all()])

admin.site.register(MotivoBajaAfijo, MotivoBajaAfijoAdmin)



#Revisado
class GrupoTrabajoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'Lista_literales','responsable','monitorInstructor','delegacion', 'provincia', 'region', 'pais', 'fechaAlta', 'fechaModificacion', 'baja', 'fechaBaja', 'motivoBajaGrupoTrabajo')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([gt.literal for gt in obj.literales.all()])

admin.site.register(GrupoTrabajo, GrupoTrabajoAdmin)



#Revisado
class MotivoBajaGrupoTrabajoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('perros/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([mbgt.literal for mbgt in obj.literales.all()])

admin.site.register(MotivoBajaGrupoTrabajo, MotivoBajaGrupoTrabajoAdmin)



#Revisado
class TipoSocioAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([ts.literal for ts in obj.literales.all()])

admin.site.register(TipoSocio, TipoSocioAdmin)
