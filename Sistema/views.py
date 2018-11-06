from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
# Correos
from django.core.mail import send_mail
# Validaciones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Importacion de Modelos
from .models import Persona, Mascota
# Importacion de Formularios
from .forms import RegistrarPersonaForm, RegistrarAdminForm, LoginForm, RecuperacionForm, RegistrarMascotaForm

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
        new.is_staff=False
        new.save()
        regDB=Persona(user=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),fechaNacimiento=data.get("fechaNacimiento"),numeroFono=data.get("numeroFono"),regionPersona=data.get("regionPersona"),ciudadPersona=data.get("ciudadPersona"),viviendaPersona=data.get("viviendaPersona"))
        regDB.save()
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas})

# Registro de Personas para Admin
def registroAdmin(request):
    personas=Persona.objects.all()
    form=RegistrarAdminForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        tipo = data.get("tipoPersona")
        if tipo == "Usuario":
            new.is_staff=False
        else:
            new.is_staff=True
        new.save()
        regDB=Persona(user=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),fechaNacimiento=data.get("fechaNacimiento"),numeroFono=data.get("numeroFono"),regionPersona=data.get("regionPersona"),ciudadPersona=data.get("ciudadPersona"),viviendaPersona=data.get("viviendaPersona"),tipoPersona=data.get("tipoPersona"))
        regDB.save()
    form=RegistrarAdminForm()
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
def olvido(request):
    form=RecuperacionForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=User.objects.get(username=data.get("username"))
        send_mail(
                'Recuperación de contraseña',
                'Haga click aquí para ingresar una nueva contraseña',
                'alexander.isaias.caru.barrera@gmail.com',
                [user.mail],
                #html_message = 'Haga click <a href="http://127.0.0.1:8000/recuperar?user='+user.username+'">aquí</a> para configurar una nueva contraseña.',
            )
    return render(request,"recover.html",{'form':form})

# def recuperar(request)
#     form=RecuperarForm(request.POST or None)
#     message=""
#     try:
#         username=request.GET["user"]
#     except Exception as e:
#         username= None
#     if username is not None:
#         if form.is_valid():
#             data=form.cleaned_data
#             if data.get("password1") == data.get("password2"):
#                 message="La contraseña se ha cambiado correctamente"
#                 contra=make_password(data.get("password2"))
#                 User.objects.filter(username=username).update(password=contra)
#             else:
#                 message="Las contraseñas no coinciden"
#         return render(request,"recuperar.html",{'form':form, 'username':username, 'message':message})
#     else:
#         return redirect('login')

# Registro de Perro
def registroPerro(request):
    perros=Mascota.objects.all()
    form=RegistrarMascotaForm(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(imagen=data.get("imagen"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascotra=data.get("descripcionMascotra"),estadoMascota=data.get("estadoMascota"))
        regDB.save()
    form = RegistrarMascotaForm()
    return render(request, "registroPerro.html", {'form': form, 'perros':perros})

# Registro de Mascota
# REGISTRO DE MASCOTA CON PERSONA
# ARREGLARR--------------------------------------------------
# def registroPerro(request):
#     perros=Mascota.objects.all()
#     form=RegistrarMascotaForm(request.POST, request.FILES)
#     if form.is_valid():
#         data=form.cleaned_data
#         regDB=Mascota(imagen=data.get("imagen"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcionMascotra=data.get("descripcionMascotra"),estadoMascota=data.get("estadoMascota"))
#         regDB.save()
#     form = RegistrarMascotaForm()
#     return render(request, "registroPerro.html", {'form': form, 'perros':perros})
