from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), # El que tiene solo comillas es la página principal
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Add this line
    path('blog/', views.blog, name='blog'),  # Add this line
    path('services/', views.services, name='services'),  # Add this line
    path('our_teams/', views.our_teams, name='our_teams'),  # Add this line
    path('portafolio/', views.portafolio, name='portafolio'),  # Add this line
    path('testimonios/', views.testimonios, name='testimonios'),  # Add this line
    path('events_register/', views.event_register_view, name='event_register'),  # Add this line
    path('events_list/', views.event_list_view, name='event_list'),  # Add this line
    path('portafolio_register/', views.portafolio_register_view, name='portafolio_register'),# Add this line
    path('testimonio_register/', views.testimonio_register_view, name='testimonio_register'),  # Add this line
    
]


