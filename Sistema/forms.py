from django import forms

# Formulario para Registro de una Persona
class RegistrarPersonaForm(forms.Form):
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

# Formulario para el Login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

# Formulario para Recuperar Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Registro de Mascota
class RegistrarMascotaForm(forms.Form):
    image = forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre")
    #---------- CAMBIAR A OPTIONS
    razaMascota=forms.CharField(widget=forms.TextInput(),label="Raza")
    #---------- CAMBIAR A TEXTAREA
    descripcionMascotra=forms.CharField(widget=forms.TextInput(),label="Descripcion")
    #---------- CAMBIAR A OPTIONS
    estadoMascota=forms.CharField(widget=forms.TextInput(),label="Estado")
