from django.contrib import admin
from .models import Idioma, Literal, Pais, Region, Provincia, Tratamiento, FormaPago

# Register your models here.


class IdiomaAdmin(admin.ModelAdmin):
    list_display = ('codigoIdioma','idioma')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }

admin.site.register(Idioma, IdiomaAdmin)


class LiteralAdmin(admin.ModelAdmin):
    list_display = ('literal','idioma')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }

admin.site.register(Literal, LiteralAdmin)


class TratamientoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([tr.literal for tr in obj.literales.all()])

admin.site.register(Tratamiento, TratamientoAdmin)


class PaisAdmin(admin.ModelAdmin):
    list_display = ('nombre','codigo', 'Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([pa.literal for pa in obj.literales.all()])

admin.site.register(Pais, PaisAdmin)


class RegionAdmin(admin.ModelAdmin):
    list_display = ('nombre','pais', 'Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([ca.literal for ca in obj.literales.all()])
    
admin.site.register(Region, RegionAdmin)


class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('nombre','region', 'Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([pr.literal for pr in obj.literales.all()])

admin.site.register(Provincia, ProvinciaAdmin)



class FormaPagoAdmin(admin.ModelAdmin):
    list_display = ('descripcion','Lista_literales')

    class Media:
        css = {
            'all': ('general/css/custom_ckeditor.css',)
        }
    def Lista_literales(self, obj):
        return "\n".join([fp.literal for fp in obj.literales.all()])

admin.site.register(FormaPago, FormaPagoAdmin)



