from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Importacion de Modelos
from .models import Persona, Mascota
# Importacion de Formularios
from .forms import RegistrarPersonaForm, LoginForm, RecuperacionForm, RegistrarMascotaForm

# Create your views here.
# Index
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Index",
    }
    return HttpResponse(plantilla.render(contexto,request))

# Registro de Personas
def registroPersona(request):
    personas=Persona.objects.all()
    form=RegistrarPersonaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Persona(rutPersona=data.get("rutPersona"),passwordPersona=data.get("passwordPersona"),nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),direccionPersona=data.get("direccionPersona"),numeroFono=data.get("numeroFono"),mailPersona=data.get("mailPersona"))
        regDB.save()
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas})

# Login
def ingreso(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('registro')
    return render(request,"login.html",{'form':form})

# Recuperacion Contraseña
def recuperar(request):
    form=RecuperacionForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
    return render(request,"recover.html",{'form':form})

# Registro de Mascota
def registroMascota(request):
    form = RegistrarMascotaForm(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(imagen=data.get("image"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascotra=data.get("descripcionMascotra"),estadoMascota=data.get("estadoMascota"))
        regDB.save()
        message = "Image uploaded succesfully!"
    else:
        form = RegistrarMascotaForm()
    return render(request, "registroMascota.html", {'form': form})
