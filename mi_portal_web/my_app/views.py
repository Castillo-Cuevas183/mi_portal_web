from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("bienvenido a tu página.")
    return render (request, 'myapp/home.html')

def about (request):
    # return HttpResponse("Estás en la sección 'Acerca de'.")
    return render (request, 'myapp/about.html')

def contact(request):
    # return HttpResponse("Estás en la sección 'Contacto'.")
    return render (request, 'myapp/contact.html')

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

def portafolio (request):
    projects =[
        {'name': 'Pagina de Restaurant', 'description': 'Proyecto para cadena de restaurantes mexicanos', 'image': '' },
        {'name': 'Pagina de Inmobiliarias', 'description': 'Proyecto para venta de casas', 'image': '' },
        {'title': 'Pagina de Escuelas', 'description': 'Descripción del proyecto 3'},
        #... more projects here
    ]
    return render(request, 'myapp/portafolio.html', {'projects': projects})


def testimonios (request):

    testimonios_data =[
        {'Nombre': "Roberto", 'Puesto': "CEO", 'testimonio': 'Excelente servicio' },
        {'Nombre': "Roberto", 'Puesto': "CEO", 'testimonio': 'Excelente servicio' },
        #... more projects here
    ]
    return render(request, 'myapp/testimonios.html', {'testimonios': testimonios_data})