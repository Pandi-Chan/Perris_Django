from django.db import models

# Create your models here.
class Persona(models.Model):
    rutPersona=models.CharField(primary_key=True, max_length=9)
    nombrePersona=models.CharField(max_length=30)
    apellidoPersona=models.CharField(max_length=30)
    fechaNacimiento=models.DateField()
    direccionPersona=models.CharField(max_length=50)
    numeroFono=models.CharField(max_length=10,null=True,blank=True)
    mailPersona=models.CharField(max_length=50)
    passwordPersona=models.CharField(max_length=30)
    def __str__(self):
        return self.nombrePersona+ " "+self.apellidoPersona

class Mascota(models.Model):
    codigoMascota=models.AutoField(primary_key=True)
    nombreMascota=models.CharField(max_length=20)
    edadMascota=models.IntegerField()
    def __str__(self):
        return self.nombreMascota

class MascotaPersona(models.Model):
    codigoMascota=models.ForeignKey(Mascota,on_delete=models.CASCADE)
    codigoPersona=models.ForeignKey(Persona,on_delete=models.CASCADE)