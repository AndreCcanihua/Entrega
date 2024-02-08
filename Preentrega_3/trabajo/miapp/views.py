from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def home(request):
    return render(request, "miapp/home.html")

def equipos(request):
    contexto = {'equipos': Equipo.objects.all()}
    return render(request, "miapp/equipos.html", contexto)

def heroes(request):
    return render(request, "miapp/heroes.html")

def villanos(request):
    contexto = {'villanos': Villano.objects.all()}   
    return render(request, "miapp/villanos.html", contexto)

def logros(request):
    return render(request, "miapp/logros.html")

def equipoForm(request):
    if request.method == "POST":
        miForm = EquipoForm(request.POST)
        if miForm.is_valid():
            equipo_nombre = miForm.cleaned_data.get("nombre")
            equipo_integrantes = miForm.cleaned_data.get("integrantes")
            equipo = Equipo(nombre=equipo_nombre, integrantes=equipo_integrantes)
            equipo.save()
            return render(request, "miapp/home.html")
                
    else:
        miForm = EquipoForm()

    return render(request, "miapp/equipoForm.html", {"form": miForm })

def villanoForm(request):
    if request.method == "POST":
        miForm = VillanoForm(request.POST)
        if miForm.is_valid():
            villano_nombre = miForm.cleaned_data.get("nombre")
            villano_identidadSecreta = miForm.cleaned_data.get("identidadSecreta")
            villano_emailContacto = miForm.cleaned_data.get("emailContacto")
            villano_poderes = miForm.cleaned_data.get("poderes")
            villano = Villano(nombre=villano_nombre, identidadSecreta=villano_identidadSecreta, emailContacto=villano_emailContacto, poderes=villano_poderes)
            villano.save()
            return render(request, "miapp/home.html")
                
    else:
        miForm = VillanoForm()

    return render(request, "miapp/villanoForm.html", {"form": miForm })

def buscar(request):
    return render(request, "miapp/buscar.html")

def buscarEquipo(request):
    if request.GET["buscar"]:
        patron = request.GET["buscar"]
        equipos = Equipo.objects.filter(nombre__icontains=patron)
        contexto = {"equipos": equipos }
        return render(request, "miapp/equipos.html", contexto)
    return HttpResponse("No se ingreso los datos necesarios")