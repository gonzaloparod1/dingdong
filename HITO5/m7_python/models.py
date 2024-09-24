from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator

# Create your models here.

class UserProfile(models.Model):
    ROLES = (('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rol = models.CharField(max_length=255, choices=ROLES, default='arrendatario')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.rol})'

#! -> accedemos al ROL así user.user_profile.rol

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
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=1500)
    m2_construidos = models.IntegerField(validators=[MinValueValidator(1)])
    m2_totales = models.IntegerField(validators=[MinValueValidator(1)])
    num_estacionamientos = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    num_habitaciones = models.IntegerField(validators=[MinValueValidator(1)], default=1)
    num_baños = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    direccion = models.CharField(max_length=255)
    tipo_inmueble = models.CharField(max_length=255, choices=TIPOS)
    precio = models.IntegerField(validators=[MinValueValidator(1000)], null=True) # precio mensual
    precio_ufs = models.FloatField(validators=[MinValueValidator(1.0)], null=True)
    disponible = models.BooleanField(default=True)
    #* UF se utiliza para ajustar los valores de contratos, precios y pagos para reflejar cambios en la inflación.
    #TODO_ FKs - llaves foráneas - 1:N
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    arrendador = models.ForeignKey(User, related_name='inmuebles', on_delete=models.RESTRICT)
    #* arrendador - propietario es un USER de de tipo rol 'arrendador' en el UserProfile
    # estado = models.CharField(max_length=255, choices=ESTADO) # <- 'nuevo', 'estrenar', 'viejo'

class Solicitud(models.Model):
    ESTADOS = (('pendiente', 'Pendiente'), ('rechazada', 'Rechazada'), ('aprobada', 'Aprobada'), ('finalizada', 'Finalizada'))
    inmueble = models.ForeignKey(Inmueble, related_name='solicitudes', on_delete=models.CASCADE)
    #* El arrendador aquí no hace falta ya que esta relación la contiene el inmueble por relación
    #! arrendador = models.ForeignKey(UserProfile, related_name='solicitudes_arrendador', on_delete=models.CASCADE) 
    arrendatario = models.ForeignKey(User, related_name='solicitudes_arrendatario', on_delete=models.CASCADE)
    #* del USER obtener first_name, last_name, email y teléfono (UserProfile)
    #* este es un USER de de tipo rol 'arrendatario' en el UserProfile
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=50, choices=ESTADOS, default='pendiente')


#________________________________________________________
# MODEL CONTACTO
class ContactForm(models.Model):
    customer_email = models.EmailField()
    customer_name = models.CharField(max_length=64)
    message = models.TextField()
    
    def __str__(self):
        return self.customer_name
  
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

REGION
cod (PK)
nombre 

COMUNA 
cod (PK)
nombre
region (FK)

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

# UserProfile.ROLES -> ["",""]
# user = UserProfile({...})
# user.ROLES -> []

"""

<select> 
value="arrendador" > Arrendador
value="arrendatario" > Arrendatario
"""