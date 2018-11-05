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
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

# Formulario para Recuperar Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Registro de Mascota
class RegistrarMascotaForm(forms.Form):
    imagen = forms.ImageField()
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre")
    razaMascota=forms.ChoiceField(choices=(('1', 'Akita Inu'),('2', 'Beagle'),('3', 'Border Collie'),('4', 'Boxer'),('5', 'Bulldog'),('6', 'Dálmata'),('7', 'Golden Retriever'),('8', 'Gran Danés'),('9', 'Labrador'),('10', 'Pastor Alemán'),('11', 'Pit Bull'),('12', 'Pug'),('13', 'Quiltro'),('14', 'Rottweiler'),('15', 'Sabueso'),('16', 'San Bernardo'),('17', 'Terrier')),label="Raza")
    descripcionMascotra=forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':30}),label="Descripcion",)
    estadoMascota=forms.ChoiceField(choices=(('1', 'Rescatado'),('2', 'Disponible'),('3', 'Adoptado')),label="Estado")
