from django.shortcuts import render
from .services import obtener_todos_los_inmuebles
from .models import  User, Inmueble, Region, Comuna, Solicitud

# Create your views here.
def indexView(request):
    
    inmuebles = Inmueble.objects.all()
    context = {
        "inmuebles": inmuebles,
    }
    return render(request,'index.html', context)