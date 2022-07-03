from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('contact/', views.contact, name='contact'),
    path('department/', views.department, name='department'),
    path('gallery/', views.gallery, name='gallery'),
    path('doctors/', views.doctors, name='doctors'),
]
