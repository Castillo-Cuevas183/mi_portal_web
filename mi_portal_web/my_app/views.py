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


