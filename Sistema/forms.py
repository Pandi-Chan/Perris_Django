from django import forms

class RegistrarPersona(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut: ")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña: ")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre: ")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido: ")
    #fechaNacimiento=forms.CharField(widget=forms.DateField(),label="Fecha Nacimiento: ")
    direccionPersona=forms.CharField(widget=forms.TextInput(),label="Direccion: ")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono: ")
    #mailPersona=forms.EmailField(widget=forms.EmailField(),label="Email: ")