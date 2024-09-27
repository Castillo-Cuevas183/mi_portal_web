from django.urls import path
from . import views 

urlpatterns = [
    path('home', views.home, name='home'), # El que tiene solo comillas es la página principal
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Add this line
    path('blog/', views.blog, name='blog'),  # Add this line
    path('services/', views.services, name='services'),  # Add this line
    path('our_teams/', views.our_teams, name='our_teams'),  # Add this line
    path('portafolio/', views.portafolio, name='portafolio'),  # Add this line
    path('testimonios/', views.testimonios, name='testimonios'),  # Add this line
]


