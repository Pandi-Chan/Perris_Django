from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Tabla Persona
class Persona(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    nombrePersona=models.CharField(max_length=30)
    apellidoPersona=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    numeroFono=models.CharField(max_length=10,null=True,blank=True)
    regionPersona=models.CharField(max_length=50)
    ciudadPersona=models.CharField(max_length=50)
    viviendaPersona=models.CharField(max_length=50)
    tipoPersona=models.CharField(max_length=50, default="usuario")
    def __str__(self):
        return self.nombrePersona+ " "+self.apellidoPersona

# Tabla Mascota
class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    imagen=models.ImageField(upload_to='./media/imagenes/')
    nombreMascota=models.CharField(max_length=20)
    razaMascota=models.CharField(max_length=50)
    descripcionMascotra=models.TextField(null=True, blank=True)
    estadoMascota=models.CharField(max_length=50,default="rescatado")

    def __str__(self):
        return self.nombreMascota

# Tabla de Relacion Persona/Mascota
class MascotaPersona(models.Model):
    codigoMascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    codigoPersona=models.ForeignKey(Persona,on_delete=models.CASCADE)
