from django import forms

class RegistrarPersona(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    #----------- CAMBIAR CAMPOS
    regionPersona=forms.ChoiceField(choices=(('1', 'First and only',),),label="Región")
    ciudadPersona=forms.ChoiceField(choices=(('1', 'First and only',),),label="Ciudad")
    #-----------------
    viviendaPersona=forms.ChoiceField(choices=(('1', 'Casa con Patio Grande'),('2', 'Casa con Patio Pequeño'),('3', 'Casa sin Patio'),('4', 'Departamento')),label="Tipo Vivienda")


class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

class Recuperacion(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")
