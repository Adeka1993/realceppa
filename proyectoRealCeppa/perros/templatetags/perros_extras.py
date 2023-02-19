from django import template
from perros.models import Perro

register = template.Library()

@register.simple_tag
def get_perro_list():
    perros = Perro.objects.all()
    return perros