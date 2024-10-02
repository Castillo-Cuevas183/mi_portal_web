from django import forms
from .models import Contact, Event, Porta, Testimonio

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'fecha', 'capacidad']

class PortaForm(forms.ModelForm):
    class Meta:
        model = Porta
        fields = ['nombre_proyecto', 'descripcion', 'image','link']

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['nombre', 'descripcion','puesto', 'empresa']