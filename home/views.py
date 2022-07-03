from django.http import HttpResponse
from django.shortcuts import render
from . models import Departments, Doctors

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def booking(request):
    return render(request, 'booking.html')
def contact(request):
    return render(request, 'contact.html')
def department(request):
    department = {
        'department': Departments.objects.all()
    }
    return render(request, 'department.html',department)
def gallery(request):
    return render(request, 'gallery.html')
def doctors(request):
    doctors = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html',doctors)