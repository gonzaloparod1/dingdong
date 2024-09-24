# PROYECTO - INMUEBLE

## HITO 1
1. Iniciar Proyecto
2. Implementar postgres SQL 
3. Crear los modelos 
4. Crear 4 servicios en nuestro services.py

## HITO 2 
1. Poblar de datos nuestra DB (data semilla - load-data)
2. Testeo de nuestra DB desde el temp.py, de dos maneras:
    - Con ORM 
    - Sin ORM (a pura consulta SQL) 
    - Vamos a escribir los resultados en un data.txt 

## HITO 3 
1. Formularios
    - Registro
    - Inicio sesión 
    - Alguna vista simple 

## HITO 4 
1. Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.
    - a. Generar las rutas para la vista para agregar nuevas viviendas.
    - b. Generar el objeto de formulario.
    - c. Agregar la función para guardar el objeto.

2. Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble existente.
    - a. Generar las rutas para la vista para actualizar las viviendas por usuario.
    - b. Generar el objeto de formulario en base a él modelo definido.
    - c. Agregar la función para actualizar el objeto.

3. Crear una página web básica donde los arrendatarios puedan ver la oferta disponible. 
    - a. Generar las rutas para ver las viviendas.
    - b. Crear la vista y el controlador que le permitan enlistar las viviendas.

---

# VISTAS

- LandingPage de Bienvenida con Registrarme || Iniciar Sesión 
    - Select para determinar TIPO_USUARIO (rol)
- Dashboard_arrendatario || Dashboard_arrendador
    - Ambos deben tener para editar su perfil 
    - Vista lista

## PROPIETARIO - ARRENDADOR
- Vista de lista de sus publicaciones
- Vista detalle de inmueble 
    - Lista de solicitudes (arrendatarios) de dicho inmueble con bttn para pasar de `pendiente` a `aprobado` o `rechazado`

1. Crear página web básica donde arrendadores puedan agregar nuevos inmuebles.
a. Generar las rutas para la vista para agregar nuevas viviendas.
b. Generar el objeto de formulario.
c. Agregar la función para guardar el objeto.

2. Crear página web básica donde arrendadores puedan actualizar/borrar un inmueble 
existente.
a. Generar las rutas para la vista para actualizar las viviendas por usuario.
b. Generar el objeto de formulario en base a él modelo definido.
c. Agregar la función para actualizar el objeto.

## INQUILINO - ARRENDATARIO
- Vista de inmuebles publicados 
- Detalle de inmueble
    - Formulario de solicitud para dicho inmueble 
3. Crear una página web básica donde los arrendatarios puedan ver la oferta disponible. 
a. Generar las rutas para ver las viviendas.
b. Crear la vista y el controlador que le permitan enlistar las viviendas.
