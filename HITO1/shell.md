
```bash
python manage.py shell

from m7_python.models import User, Inmueble, Comuna, Region, Solicitud 
from m7_python.services import crear_inmueble, obtener_todos_los_inmuebles, actualizar_descripcion_inmueble, eliminar_inmueble, crear_comuna, crear_region, crear_usuario, actualizar_descripcion_inmueble

crear_inmueble('Casa 2 pisos','Grande y lujosa con patio','110.00','4','2','3','Clavel 1834','Casa','10000000','ABC','True','1')

# crear_inmueble 
# obtener_todos_los_inmuebles 
# actualizar_descripcion_inmueble / update
# eliminar_inmueble - baneo (softDelete) -> is_active

