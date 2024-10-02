from django.contrib import admin
from .models import Event, Porta, Testimonio, Contact

# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'fecha', 'capacidad']
    search_fields = ['name']  # Cambiado a lista o podrías usar ('name',)

admin.site.register(Event, EventAdmin)


class PortaAdmin(admin.ModelAdmin):
    list_display = ['nombre_proyecto', 'descripcion', 'image', 'link']
    search_fields = ['nombre_proyecto']  # Cambiado a lista o podrías usar ('nombre_proyecto',)

admin.site.register(Porta, PortaAdmin)

class TestimonioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'descripcion', 'puesto', 'empresa']
    search_fields = ['nombre']  # Cambiado a lista o podrías usar ('nombre_proyecto',)

admin.site.register(Testimonio, TestimonioAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')
    search_fields = ('nombre',)  # Cambiado a lista o podrías usar ('nombre_proyecto',)

admin.site.register(Contact, ContactAdmin)
