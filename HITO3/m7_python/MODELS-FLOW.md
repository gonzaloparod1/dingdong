

```py
class UserProfile(models.Model):
    ROLES = (('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    # ... ... 
    rol = models.CharField(max_length=255, choices=ROLES, default='arrendatario')

class Region(models.Model):
    cod = models.CharField(max_length=2, primary_key=True)
    nombre = models.CharField(max_length=255)

class Comuna(models.Model):
    cod = models.CharField(max_length=5, primary_key=True)
    nombre = models.CharField(max_length=255)
    region = models.ForeignKey(Region, related_name='comunas', on_delete=models.RESTRICT)


class Inmueble(models.Model):
    TIPOS = (('casa', 'Casa'), ('departamento', 'Departamento'), ('bodega', 'Bodega'), ('parcela', 'Parcela'))
    nombre = models.CharField(max_length=50)
    # ... ... 
    disponible = models.BooleanField(default=True)
    #TODO_ FKs - llaves foráneas - 1:N
    comuna = models.ForeignKey(Comuna, related_name='inmuebles', on_delete=models.RESTRICT)
    arrendador = models.ForeignKey(User, related_name='inmuebles', on_delete=models.RESTRICT)
    # arrendador

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
```


# ARRENDADOR - PROPIETARIO (flow)
userArrendador.inmuebles -> [{},{}]
userArrendador.inmuebles[0].solicitudes -> [{},{},{}]
userArrendador.inmuebles[0].solicitudes[2].arrendatario -> {} 
userArrendador.inmuebles[0].solicitudes[2].estado -> "pendiente" 

# ARRENDATARIO - INQUILINO (flow)
UserInquilino.solicitudes_arrendatario -> [{},{},{}]
UserInquilino.solicitudes_arrendatario[0].inmueble -> {}
UserInquilino.solicitudes_arrendatario[0].estado -> "pendiente" 
UserInquilino.solicitudes_arrendatario[0].inmueble.arrendador -> {}  <- (propietario)
UserInquilino.solicitudes_arrendatario[0].inmueble.comuna -> {}
UserInquilino.solicitudes_arrendatario[0].inmueble.comuna.region -> {}

# INMUEBLE (flow)
Inmueble.objects.all() <- arrendatario (Inquilino) accede a todos los inmuebles
