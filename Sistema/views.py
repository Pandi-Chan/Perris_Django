from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
# Correos
from django.core.mail import send_mail
# Validaciones
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Importacion de Modelos
from .models import Persona, Mascota
# Importacion de Formularios
from .forms import RegistrarPersonaForm, RegistrarAdminForm, LoginForm, RecuperacionForm, RegistrarMascotaForm, RestablecerForm

# Create your views here.
#------------------------------------------ INDEX ------------------------------------------
def index(request):
    plantilla=loader.get_template("index.html")
    return HttpResponse(plantilla.render({'titulo':"Mis Perris"},request))

# ------------------------------------------ FORMULARIOS ------------------------------------------
# Registro de Personas (DESDE FUERA DEL SISTEMA, USUARIOS NUEVOS)
def registroPersona(request):
    mensaje=""
    registro=1 #Dependiendo este número, es el Formulario que Mostrará
    personas=Persona.objects.all()
    form=RegistrarPersonaForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        new.is_staff=False
        new.save()
        regDB=Persona(user=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),fechaNacimiento=data.get("fechaNacimiento"),numeroFono=data.get("numeroFono"),regionPersona=data.get("regionPersona"),ciudadPersona=data.get("ciudadPersona"),viviendaPersona=data.get("viviendaPersona"))
        regDB.save()
        mensaje='Usuario '+regDB.nombrePersona+' Registrado'
    form=RegistrarPersonaForm()
    return render(request,"registro.html",{'form':form,'personas':personas,'registro':registro,'titulo':"Registro",'mensaje':mensaje})

# Registro de Personas para Admin (DESDE DENTRO DEL SISTEMA)
@login_required(login_url='login')
def registroAdmin(request):
    actual=request.user
    mensaje=""
    registro=2 # Dependiendo este Numero es el Formulario que Mostrará
    personas=Persona.objects.all()
    form=RegistrarAdminForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        new=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        # Tipo es Tomado del Formulario (El ComboBox/ChoiceField)
        tipo = data.get("tipoPersona") # Lo Guardo en una Variable para evitar posibles Problemas
        if tipo == 'Usuario': # Verifica el Texto tomado del ComboBox/ChoiceField
            new.is_staff=False # El is_staff es un campo que viene con la clase USER, es para diferenciar los tipos de usuario,
            # SI es un usuario normal, queda en False
        else:
            # Pero si tiene como Tipo "Admnistrador", queda en True. Gracias a esto puedes hacer la diferencia en el HTML Maqueta
            new.is_staff=True
        new.save() # IMPORTANTE PONERLE SAVE Y RECORDAR QUE LOS USUARIOS CREADOS DESDE QUE EDITAS ESTO SON LOS QUE TENDRAN LOS PRIVILEGIOS DE Admin
        regDB=Persona(user=new,nombrePersona=data.get("nombrePersona"),apellidoPersona=data.get("apellidoPersona"),fechaNacimiento=data.get("fechaNacimiento"),numeroFono=data.get("numeroFono"),regionPersona=data.get("regionPersona"),ciudadPersona=data.get("ciudadPersona"),viviendaPersona=data.get("viviendaPersona"),tipoPersona=data.get("tipoPersona"))
        regDB.save()
        mensaje='Usuario '+regDB.nombrePersona+' Registrado'
    form=RegistrarAdminForm()
    return render(request,"registro.html",{'form':form,'personas':personas,'actual':actual,'registro':registro,'titulo':"Registro",'mensaje':mensaje})

# Registro de Perro NUEVO (RESCATADO O DISPONIBLE)
@login_required(login_url='login')
def registroPerro(request):
    actual=request.user
    mensaje=""
    perros=Mascota.objects.all()
    form=RegistrarMascotaForm(request.POST, request.FILES)
    if form.is_valid():
        data=form.cleaned_data
        regDB=Mascota(imagen=data.get("imagen"),nombreMascota=data.get("nombreMascota"),razaMascota=data.get("razaMascota"),descripcion=data.get("descripcion"),estadoMascota=data.get("estadoMascota"))
        regDB.save()
        mensaje='Perro '+regDB.nombreMascota+' Registrado'
    form = RegistrarMascotaForm()
    return render(request, "registroPerro.html", {'form': form, 'perros':perros, 'actual':actual,'titulo':"Registro Perro",'mensaje':mensaje})

# Registro de Mascota (ADOPCION)
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
#     return render(request, "registroPerro.html", {'form': form, 'perros':perros,'titulo':"Registro Adopcion",})

# ------------------------------------------ AUTENTICACIONES y USUARIOS ------------------------------------------
# Login
def ingreso(request):
    mensaje=""
    form=LoginForm(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            mensaje='Datos Invalidos'
    return render(request,"login.html",{'form':form,'titulo':"Login",'mensaje':mensaje})

# Logout
def salir(request):
    logout(request)
    return redirect('/index/')

# Recuperacion Contraseña
def olvido(request):
    form=RecuperacionForm(request.POST or None)
    mensaje=""
    if form.is_valid():
        data=form.cleaned_data
        user=User.objects.get(username=data.get("username"))
        send_mail(
                'Recuperación de contraseña',
                'Haga click aquí para ingresar una nueva contraseña',
                'perrisfeos@gmail.com',
                [user.email],
                html_message = 'Pulse <a href="http://localhost:8000/restablecer?user='+user.username+'">aquí</a> para restablecer su contraseña.',
            )
        mensaje='Correo Enviado a '+user.email
    return render(request,"olvido.html",{'form':form, 'mensaje':mensaje, 'titulo':"Recuperar Contraseña",})

# Restablecer Contraseña
def restablecer(request):
    form=RestablecerForm(request.POST or None)
    mensaje=""
    try:
        username=request.GET["user"]
    except Exception as e:
        username= None
    if username is not None:
        if form.is_valid():
            data=form.cleaned_data
            if data.get("password_A") == data.get("password_B"):
                mensaje="La contraseña se ha restablecido"
                contra=make_password(data.get("password_B"))
                User.objects.filter(username=username).update(password=contra)
            else:
                mensaje="Las contraseñas no coinciden"
        return render(request,"restablecer.html",{'form':form, 'username':username, 'mensaje':mensaje, 'titulo':"Restablecer Contraseña",})
    else:
        return redirect('/login/')

# ------------------------------------------ GESTION ------------------------------------------
# Lista de Perros
@login_required(login_url='login')
def listaPerro(request):
    actual=request.user
    perros=Mascota.objects.all()
    return render (request,"listaPerro.html",{'perros':perros,'actual':actual,'titulo':"Lista de Perros",})

# Lista de Personas
@login_required(login_url='login')
def listaPersona(request):
    actual=request.user
    personas=Persona.objects.all()
    return render (request,"listaPersona.html",{'personas':personas,'actual':actual,'titulo':"Lista de Personas",})
