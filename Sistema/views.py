from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader 

# Create your views here.
def index(request):
    plantilla=loader.get_template("index.html")
    contexto={
        'titulo':"Index",
    }
    return HttpResponse(plantilla.render(contexto,request))
