from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrarPersona
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Index",
    }
    return HttpResponse(plantilla.render(contexto,request))

def registro(request):
    form=RegistrarPersona(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        u=User.objects.create_user(data.get("rutPersona"),data.get("mailPersona"),data.get("passwordPersona"))
        u.save()
    form=RegistrarPersona()
    return render(request,"Registro.html",{'form':form,})