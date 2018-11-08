from django import forms
#Tupla de Regiones
regiones=(('Arica y Parinacota','Arica y Parinacota'),('Tarapacá','Tarapacá'),('Antofagasta','Antofagasta'),
    ('Atacama','Atacama'),
    ('Coquimbo','Coquimbo'),
    ('Valparaiso','Valparaiso'),
    ('Metropolitana de Santiago','Metropolitana de Santiago'),
    ("Libertador General Bernardo O'Higgins","Libertador General Bernardo O'Higgins"),
    ('Maule','Maule'),
    ('Biobío','Biobío'),
    ('La Araucanía','La Araucanía'),
    ('Los Ríos','Los Ríos'),
    ('Los Lagos','Los Lagos'),
    ('Aisén del General Carlos Ibáñez del Campo','Aisén del General Carlos Ibáñez del Campo'),
    ('Magallanes y de la Antártica Chilena','Magallanes y de la Antártica Chilena'),
    ('Ñuble','Ñuble'),)

tipos=(('Casa con Patio Grande', 'Casa con Patio Grande'),('Casa con Patio Pequeño', 'Casa con Patio Pequeño'),('Casa sin Patio', 'Casa sin Patio'),('Departamento', 'Departamento'))

razas=(('Akita Inu','Akita Inu'),('Beagle','Beagle'),('Border Collie','Border Collie'),('Boxer','Boxer'),('Bulldog','Bulldog'),('Dálmata','Dálmata'),('Golden Retriever','Golden Retriever'),
    ('Gran Danés','Gran Danés'),('Labrador','Labrador'),('Pastor Alemán','Pastor Alemán'),('Pit Bull','Pit Bull'),('Pug','Pug'),('Quiltro','Quiltro'),('Rottweiler','Rottweiler'),
    ('Sabueso','Sabueso'),('San Bernardo','San Bernardo'),('Terrier','Terrier'))

# Formulario para Registro de una Persona
class RegistrarPersonaForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    regionPersona=forms.ChoiceField(choices=(regiones),label="Región")
     # -------------- CAMBIAR
    ciudadPersona=forms.ChoiceField(choices=(('1', 'First and only',),),label="Ciudad")
    #-----------------
    viviendaPersona=forms.ChoiceField(choices=(tipos),label="Tipo Vivienda")

# Formulario para Registro de una Persona DESDE EL ADMIN
class RegistrarAdminForm(forms.Form):
    rutPersona=forms.CharField(widget=forms.TextInput(),label="Rut")
    passwordPersona=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")
    nombrePersona=forms.CharField(widget=forms.TextInput(),label="Nombre")
    apellidoPersona=forms.CharField(widget=forms.TextInput(),label="Apellido")
    mailPersona=forms.EmailField(label="Email: ")
    fechaNacimiento=forms.DateField(widget=forms.SelectDateWidget(years=range(1910,2001)),label="Fecha de Nacimiento")
    numeroFono=forms.CharField(widget=forms.TextInput(),label="Telefono")
    regionPersona=forms.ChoiceField(choices=(regiones),label="Región")
    # -------------- CAMBIAR
    ciudadPersona=forms.ChoiceField(choices=(('1', 'First and only',),),label="Ciudad")
    #-----------------
    viviendaPersona=forms.ChoiceField(choices=(tipos),label="Tipo Vivienda")
    tipoPersona=forms.ChoiceField(choices=(('Usuario', 'Usuario'),('Administrador','Administrador'),),label="Tipo de Usuario")

# Formulario para el Login
class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut de Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="Contraseña")

# Formulario para Email Restablece Contraseña
class RecuperacionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Rut")

# Formulario para Restablecer Contraseña
class RestablecerForm(forms.Form):
    password_A=forms.CharField(widget=forms.PasswordInput(),label="Nueva Contraseña")
    password_B=forms.CharField(widget=forms.PasswordInput(),label="Repita Contraseña")

# Formulario para Registro de Mascota
class RegistrarMascotaForm(forms.Form):
    imagen=forms.ImageField(label="Foto del Perro")
    nombreMascota=forms.CharField(widget=forms.TextInput(),label="Nombre")
    razaMascota=forms.ChoiceField(choices=(razas),label="Raza")
    descripcion=forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'cols':30}),label="Descripcion",)
    estadoMascota=forms.ChoiceField(choices=(('Rescatado', 'Rescatado'),('Disponible', 'Disponible'),('Adoptado', 'Adoptado')),label="Estado")
