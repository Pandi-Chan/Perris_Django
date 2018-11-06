from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Validaciones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
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
        new=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        regDB=Persona(user=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),fechaNacimiento=data.get("fechaNacimiento"),numeroFono=data.get("numeroFono"),regionPersona=data.get("regionPersona"),ciudadPersona=data.get("ciudadPersona"),viviendaPersona=data.get("viviendaPersona"))
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
            return redirect('/')
    return render(request,"login.html",{'form':form})

def salir(request):
    logout(request)
    return redirect('/index/')

# Recuperacion Contraseña
def recuperar(request):
    form=RecuperacionForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
    return render(request,"recover.html",{'form':form})

# Registro de Mascota
# @login_required(login_url='login')
def registroPerro(request):
    #actual=request.user
    perros=Mascota.objects.all()
    form=RegistrarMascotaForm(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(imagen=data.get("imagen"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascotra=data.get("descripcionMascotra"),estadoMascota=data.get("estadoMascota"))
        regDB.save()
    form = RegistrarMascotaForm()
    return render(request, "registroPerro.html", {'form': form, 'perros':perros})
