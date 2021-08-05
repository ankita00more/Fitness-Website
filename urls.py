from django.urls import path
from . import views

urlpatterns = [
    path('home', views.index, name='home'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('male', views.male, name='male'),
    path('female', views.female, name='female'),
    path('thank', views.thank, name='thank'),
    path('failed', views.failed, name='failed')
]
