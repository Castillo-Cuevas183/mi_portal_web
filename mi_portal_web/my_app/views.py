from django.http import HttpResponse
from django.shortcuts import render, redirect
from .form import ContactForm, EventForm, PortaForm, TestimonioForm
from .models import Event 
from .models import Porta 
from .models import Testimonio

def home(request):
    # return HttpResponse("bienvenido a tu página.")
    return render (request, 'myapp/home.html')

def about (request):
    # return HttpResponse("Estás en la sección 'Acerca de'.")
    return render (request, 'myapp/about.html')

# def contact(request):
#     # return HttpResponse("Estás en la sección 'Contacto'.")
#     return render (request, 'myapp/contact.html')

def contact(request):
    if request.method == 'POST':
     form = ContactForm(request.POST)
     if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = ContactForm()
    return render(request,'myapp/contact.html',{'form': form})


def blog (request):
    # return HttpResponse("Estás en la sección 'Blog'.")
    return render (request, 'myapp/blog.html')

def services (request):
    # return HttpResponse("Estás en la sección 'Services'.")
    return render (request, 'myapp/services.html')

def our_teams (request):
    return render (request, 'myapp/our_teams.html')

# def portafolio (request):
#     return render (request, 'myapp/portafolio.html')

# def portafolio (request):
#     projects =[
#         {'name': 'Pagina de Restaurant', 'description': 'Proyecto para cadena de restaurantes mexicanos', 'image': '' },
#         {'name': 'Pagina de Inmobiliarias', 'description': 'Proyecto para venta de casas', 'image': '' },
#         {'title': 'Pagina de Escuelas', 'description': 'Descripción del proyecto 3'},
#         #... more projects here
#     ]
#     return render(request, 'myapp/portafolio.html', {'projects': projects})


# def testimonios (request):

#     testimonios_data =[
#         {'Nombre': "Roberto", 'Puesto': "CEO", 'testimonio': 'Excelente servicio' },
#         {'Nombre': "Roberto", 'Puesto': "CEO", 'testimonio': 'Excelente servicio' },
#         #... more projects here
#     ]
#     return render(request, 'myapp/testimonios.html', {'testimonios': testimonios_data})

def event_register_view(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()
    return render(request, 'myapp/event_register.html', {'form': form})

def event_list_view(request):
    events = Event.objects.all()  #Select  * form Events
    return render (request, 'myapp/event_list.html', {'events': events} )


# Crear el modelo para portafolio y testimonios 
# Crear formularios alta de testimonios y portafolio

# Portafolio
def portafolio_register_view(request):
    if request.method == 'POST':
        form = PortaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('portafolio')
    else:
        form = PortaForm()
    return render(request, 'myapp/portafolio_register.html', {'form': form})


def portafolio (request):
    projects = Porta.objects.all()
    return render(request, 'myapp/portafolio.html', {'projects': projects})

# Testimonios
def testimonio_register_view(request):
    if request.method == 'POST':
        form = TestimonioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('testimonios')
    else:
        form = TestimonioForm()
    return render(request, 'myapp/testimonio_register.html', {'form': form})

def testimonios (request):
    testimonios_data = Testimonio.objects.all()
    return render(request, 'myapp/testimonios.html', {'testimonios': testimonios_data})