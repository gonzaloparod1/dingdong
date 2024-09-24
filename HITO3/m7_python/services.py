from .models import Inmueble, Comuna, User, Region, UserProfile

#TODO_ Services Extras - Crear Region - Crear Comuna - Crear User


def get_or_create_user_profile(user):
    try:
        # Intenta obtener el perfil del usuario o crearlo si no existe
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        if created:
            print("Se ha creado un nuevo perfil para el usuario.")
        else:
            print("El perfil ya existía.")
        return user_profile
    except Exception as e:
        print(f'Error al obtener o crear el perfil del usuario. {e}')
        return None

def create_user(new_user):
    user = User.objects.create_user(
        username=new_user['username'],
        email=new_user['email'],
        first_name=new_user['first_name'],
        last_name=new_user['last_name'],
        password=new_user['password']
    )
    return user
# create_user({username:"...", email: ... .... })

def create_user_by_params(username,email,first_name,last_name,password):
    user = User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
    )
    return user
# create_user_by_params("mau", "m@gmail.com", "mauro" .... ....)

def create_region(cod, nombre): 
    # region = Region.objects.create(cod=cod, nombre=nombre)
    region = Region(cod=cod, nombre=nombre)
    region.save()
    return region

def create_comuna(cod, nombre, region_cod):
    region = Region.objects.get(cod=region_cod)
    # region.nombre = "tata"
    # region.save()
    comuna = Comuna.objects.create(cod=cod, nombre=nombre, region= region)
    return comuna

# Van nuestros Servicios
#* ORM ->  MANGER <- objects       objects = Manager(.....)

"""
a. Crear un objeto con el modelo.
b. Enlistar desde el modelo de datos.
c. Actualizar un registro en el modelo de datos.
d. Borrar un registro del modelo de datos utilizando un modelo Django.

"""

def insertar_inmueble(data):
    """
    Inserta un nuevo inmueble en la base de datos.
    Parámetros:
        data (dict): Un diccionario con la información del inmueble a insertar.
            {
                'id_user': int,
                'tipo_inmueble': str,
                'comuna_cod': str,
                'nombre': str,
                'descripcion': str,
                'm2_totales': int,
                'm2_construidos': int,
                'num_baños': int,
                'num_habitaciones': int,
                'num_estacionamientos': int,
                'direccion': str,
                'precio': int,
                'precio_ufs': float
            }
    """
    # Obtener el usuario (arrendador) por ID
    arrendador = User.objects.get(id=data['id_user'])
    # Obtener la comuna por código (cod)
    comuna = Comuna.objects.get(cod=data['comuna_cod'])
    
     # Crear un nuevo Inmueble usando los datos proporcionados
    inmueble = Inmueble(
        arrendador=arrendador,
        tipo_inmueble=data['tipo_inmueble'],
        comuna=comuna,
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        m2_construidos=data['m2_construidos'],
        m2_totales=data['m2_totales'],
        num_baños=data['num_baños'],
        num_habitaciones=data['num_habitaciones'],
        num_estacionamientos=data.get('num_estacionamientos', 0),
        direccion=data['direccion'],
        precio=data.get('precio', None),
        precio_ufs=data.get('precio_ufs', None)
        # disponible al no pasar por defecto es True
    )
    inmueble.save()
    return inmueble

def get_all_inmuebles():
    inmuebles = Inmueble.objects.all()
    return inmuebles


def actualizar_disponibilidad_inmueble(id_inmueble, disponible):
    """
    Actualiza la disponibilidad de un inmueble existente.
    Parámetros:
        id_inmueble (int): ID del inmueble a actualizar.
        disponible (bool): Nueva disponibilidad para el inmueble.
    Retorna:
        dict: Resultado de la operación con un mensaje de éxito o error.
    """
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)  # Buscar el inmueble por ID
        # Actualizar la disponibilidad
        inmueble.disponible = disponible
        # inmueble.direccion = direccion
        # inmueble.descripcion = descripcion
        
        inmueble.save()  # Guardar los cambios
        return {
            "success": True,
            "message": "Disponibilidad actualizada con éxito"
        }
    except Inmueble.DoesNotExist:
        return {
            "success": False,
            "message": "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al actualizar la disponibilidad del inmueble: {str(e)}"
        }

def eliminar_inmueble(id_inmueble):
    """
    Elimina un inmueble de la base de datos si existe.
    Parámetros:
        id_inmueble (int): ID del inmueble a eliminar.
    Retorna:
        dict: Resultado de la operación con un mensaje de éxito o error.
    """
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)  # Buscar el inmueble por ID
        # Eliminar el inmueble
        inmueble.delete()
        return {
            "success": True,
            "message": "Inmueble eliminado con éxito"
        }
    except Inmueble.DoesNotExist:
        return {
            "success": False,
            "message": "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al eliminar el inmueble: {str(e)}"
        }
    
# crear_inmueble 
# obtener_todos_los_inmuebles 
# actualizar_descripcion_inmueble / update
# eliminar_inmueble - baneo (softDelete) -> is_active


"""
MODELOS de SERVICES

CREATE ({... ... ...})

UPDATE (id - data por actualizar -> {})

DELETE (id) 

SEARCH_UNO (ID || PK -> cod -> email ) <- SEARCH_UNO (ID) 

SEARCH_CIERTAS_COSAS FILTER (nombre || precio) 


ADMIN
def obtener_arrendadores():
    arrendadores = UserProfile.objects.filter(rol='arrendador')
    return arrendadores
"""