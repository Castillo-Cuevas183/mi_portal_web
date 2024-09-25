from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'), # El que tiene solo comillas es la página principal
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),  # Add this line
    path('blog/', views.blog, name='blog'),  # Add this line
    path('services/', views.services, name='services'),  # Add this line
]


