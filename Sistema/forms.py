from django import forms

class RegistrarPersona(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    #        Arreglar FECHA NACIMIENTO
    #fechaNacimiento=forms.DateField(widget=forms.DateInput(),label="Fecha de Nacimiento")
    #-------------------------------------
    direccionPersona=forms.CharField(widget=forms.TextInput(),label="Direccion")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    mailPersona=forms.EmailField(label="Email: ")

class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
