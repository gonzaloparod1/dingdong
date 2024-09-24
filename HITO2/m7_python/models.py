from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    ROLES=(('arrendador', 'Arrendador'),('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_profile')
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=9, null=True)
    rol= models.CharField(max_length=50, choices=ROLES, default='arrendatario')
    rut = models.CharField(max_length=9) 
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.rol})'

class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'

class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.RESTRICT)
    
    def __str__(self) -> str:
        return f'{self.nombre} ({self.cod})'
    
class Inmueble(models.Model):
    TIPOS = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
    nombre = models.CharField(max_length=50, null=True, blank=True)
    descripcion = models.TextField(max_length=500)
    m2_construidos = models.FloatField(default=0)
    num_estacionamientos = models.IntegerField(default=0)
    num_habitaciones = models.IntegerField(default=0)
    num_baños = models.IntegerField(default=0)
    direccion = models.CharField(max_length=30)
    tipo_inmueble = models.CharField(max_length=255, choices=TIPOS)
    precio_mensual = models.FloatField(default=0)
    comuna = models.ForeignKey(Comuna, on_delete=models.RESTRICT, related_name='inmuebles')
    disponible = models.BooleanField(default=True)
    arrendador = models.ForeignKey(User, on_delete=models.RESTRICT, related_name='inmuebles')
    def __str__(self):
        return f'{self.nombre} {self.descripcion} {self.comuna}'

class Solicitud(models.Model):
    rol = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'), ('finalizada', 'Finalizada'))
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes', on_delete=models.CASCADE)
    #* El arrendador aquí no hace falta ya que esta relación la contiene el inmueble por relación
    #! arrendador = models.ForeignKey(UserProfile, related_name='solicitudes_arrendador', on_delete=models.CASCADE) 
    arrendatario = models.ForeignKey(User, related_name='solicitudes_arrendatario', on_delete=models.CASCADE)
    #* del USER obtener first_name, last_name, email y teléfono (UserProfile)
    #* este es un USER de de tipo rol 'arrendatario' en el UserProfile
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=rol, default='pendiente')

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) # -> asocición - relación
#     telefono 
#     direccion 
#     rut 
#     tipo_usuario || rol ('arrendatario', 'arrendador')
#     def __str__(self):
#         return self.user.username

"""
Un nuevo usuario se debe poder:
a. Lograr registrarse en la aplicación.
b. Actualizar sus datos.
c. Poder identificarse como arrendatario o como arrendador
Además, un usuario debe tener las siguientes características:

USUARIO
--------------------------------------------------------
USER
● Nombres              (NO CREAR ESTO)
● Apellidos            (NO CREAR ESTO)
● Correo electrónico   (NO CREAR ESTO)
--------------------------------------------------------
USER-PROFILE
ROLES = (('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'))
user = models.OneToOneField(auth.User) 
● rut
● direccion
● telefono 
● rol || tipo_usuario  <- choices=ROLES, default='arrendatario'

2. Un usuario tipo arrendatario debe poder:
a. Listar las propiedades de diversas propiedades de una comuna específica.
b. Poder generar una solicitud de arriendo a la propiedad.
Además, el inmueble debe tener las siguientes caracteristicas:

INMUEBLE
TIPOS = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
● nombre (título (Ej: Casa de dos plantas))
● descripcion
● m2_construidos
● m2_totales 
● num_estacionamientos
● num_habitaciones
● num_baños
● direccion
● tipo_inmueble  -  choices=TIPOS
    ○ casa
    ○ departamento
    ○ bodega
    ○ parcela
● precio_mensual 
● comuna (FK)
● propietario (FK) - arrendador

COMUNA 
cod (PK)
nombre
region (FK)

REGION
cod (PK)
nombre 

SOLICITUD 
ESTADOS = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'),  ('finalizada', 'Finalizada'))
estado  choices=ESTADOS, default='pendiente'
fecha = models.DateTimeField(auto_now_add=True)
inmueble  (FK)  related_name = 'solicitudes'
arrendatario  (User) (FK) related_name='solicitudes_arrendatario'
#* del USER obtener first_name, last_name, email y teléfono (UserProfile)

---

inmueble.solicitudes_arrendatario: [{},{}]



3. Un usuario tipo arrendador debe poder:
a. Publicar sus propiedades en una comuna determinada con sus
características.
b. Listar propiedades en el dashboard.
c. Eliminar y editar sus propiedades.
d. Aceptar arrendatarios.

"""


"""
Ejemplo Model - Jorge R.
class UserProfile(models.Model):
    ROLES=(('arrendador', 'Arrendador'),('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=9) 
    direccion =models.CharField(max_length=100)
    telefono = models.CharField(max_length=9)
    rol=models.CharField(max_length=50, choices=ROLES, default='arrendador')
    def __str__(self):
        return f'{self.user.username}'
"""