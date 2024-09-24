from datetime import date
from .models import User, Inmueble, Comuna, Region, Solicitud



#* ORM ->  MANGER <- objects       objects = Manager(.....)
def crear_usuario(username, email, first_name, last_name, password):
    usuario = User.objects.create_user(
        username=username,
        email=email,
        first_name=first_name,
        last_name=last_name,
        password=password
        )
    return usuario

def crear_inmueble(nombre, descripcion, m2_construidos, num_estacionamientos, num_habitaciones, num_baños, direccion, tipo_inmueble,precio_mensual,comuna,disponible,arrendador):
    nuevo_inmueble = Inmueble(nombre=nombre,
                            descripcion=descripcion,
                            m2_construidos=m2_construidos,
                            num_estacionamientos=num_estacionamientos,
                            num_habitaciones=num_habitaciones,
                            num_baños=num_baños,
                            direccion=direccion,
                            tipo_inmueble=tipo_inmueble,
                            precio_mensual=precio_mensual,
                            comuna=comuna,
                            disponible=disponible,
                            arrendador=arrendador)
    nuevo_inmueble.save()    
    return nuevo_inmueble

def obtener_todos_los_inmuebles():
    todos_los_inmuebles = Inmueble.objects.all()
    return todos_los_inmuebles

def actualizar_descripcion_inmueble(id_inmueble, disponible):
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble) # Buscar el inmueble por ID
        # Actualizar la disponibilidad
        inmueble.disponible = disponible
        # inmueble.direccion = direccion
        # inmueble.descripcion = descripcion
        inmueble.save()
        return {
            "success": True,
            "message": "Disponibilidad actualizada con exito",
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
    try:
        inmueble = Inmueble.objects.get(pk=id_inmueble)
        inmueble.delete()
        return {
            "success": True,
            "message":"Inmueble eliminado con exito"
        }
    except Inmueble.DoesNotExist:
        return {
            "success": False,
            "message": "Inmueble no encontrado"
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al eliminar el inmueble {str(e)}"
        }
    
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

"""
a. Crear un objeto con el modelo.
b. Enlistar desde el modelo de datos.
c. Actualizar un registro en el modelo de datos.
d. Borrar un registro del modelo de datos utilizando un modelo Django.
"""

# crear_inmueble 
# obtener_todos_los_inmuebles 
# actualizar_descripcion_inmueble / update
# eliminar_inmueble - baneo (softDelete) -> is_active