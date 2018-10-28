from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrarPersona, LoginForm, Recuperacion
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Persona

# Create your views here.
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Index",
    }
    return HttpResponse(plantilla.render(contexto,request))

def registro(request):
    personas=Persona.objects.all()
    form=RegistrarPersona(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Persona(rutPersona=data.get("rutPersona"),passwordPersona=data.get("passwordPersona"),nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),direccionPersona=data.get("direccionPersona"),numeroFono=data.get("numeroFono"),mailPersona=data.get("mailPersona"))
        regDB.save()
    form=RegistrarPersona()
    return render(request,"registro.html",{'form':form,'personas':personas})

def ingreso(request):
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('registro')
    return render(request,"login.html",{'form':form})

def recuperar(request):
    form=Recuperacion(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
    return render(request,"recover.html",{'form':form})
