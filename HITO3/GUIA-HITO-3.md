# PROYECTO - INMUEBLE

**En las pruebas tècnicas no se menciona ni solicita el uso de `.env` (variables de entorno), pero cabe aclarar que es una buena práctica el implementarlas**

## HITO 1
1. Iniciar Proyecto
2. Implementar postgres SQL 
3. Crear los modelos 
4. Crear 4 servicios en nuestro services.py

---

## HITO 2 
1. Poblar de datos nuestra DB (data semilla - load-data)
    - a. Poblar la base de datos con todas las regiones y comunas de Chile usando loaddata. 
    - b. Poblar de tipos de inmuebles en la base de datos usando loaddata. 
    - c. Poblar la base de datos con varios inmuebles y usuarios usando loaddata. 

2. Testeo de nuestra DB desde el temp.py, de dos maneras:
    - Con ORM 
    - Sin ORM (a pura consulta SQL) 
    - Vamos a escribir los resultados en un outputs/data.txt 

Son 4 consultas (siendo cada una de estos puntos en ORM (DJango) y SQL puro):
- Consultar listado de inmuebles para arriendo separado por comunas, solo usando los 
campos "nombre" y "descripción" en un script python que se conecta a la DB usando 
DJango y SQL guardando los resultados en un archivo de texto.

- Consultar listado de inmuebles para arriendo separado por regiones en un script 
python que se conecta a la DB usando DJango y SQL guardando los resultados en un 
archivo de texto 
    
3. Vista Lista Inmuebles
    - ● Generar enrutamiento. 
    - ● Importar el modelo en la Vista. 
    - ● Crear el Template. 
    - ● Exponer los datos en la vista

## .env

```bash
ENGINE=django.db.backends.postgresql
NAME=hito_b
USER=postgres
HOST=127.0.0.1
PORT=5432
PASSWORD=1234

DEBUG=True

TEST_ENV= test-.env

DJANGO_SETTINGS_MODULE=mysite.settings
DJANGO_SETTINGS_TEST=hola-mundo-temp
```


---

## HITO 3 
- Armar estructura Html
    - base.html 
    - navBar.html
    - footer.html
    - about.html
- Formularios
    - Registro
    - Inicio sesión 
    - Alguna vista simple 

```py
 path('',views.indexView,name='home'), # LIST Inmuebles - Redirect (Bifurcación)
 path('dashboard/',views.dashboardView,name='dashboard'), # Vista principal del Arrendador

 path('login/',LoginView.as_view(),name='login_url'), # FORMS
 path('logout/',LogoutView.as_view(next_page='home'),name='logout'), # FORMS

 path('register/',views.registerView,name='register_url'), # FORMS
 path('register_tipo/',views.register_tipoView,name='register_tipo_url'), # FORMS

 path('view_profile/',views.profile,name='profile'), # No Forms
 path('udpate_profile/',views.profile,name='update_profile'), # FORMS
```
## Etapas HITO 3
1. Formularios `login` y `logout`
    - `registration/login`
    - `registration/logout`
```bash
 path('login/',LoginView.as_view(),name='login_url'), # FORMS
 path('logout/',LogoutView.as_view(next_page='home'),name='logout'), # FORMS
```
`https://docs.djangoproject.com/en/5.1/topics/auth/default/`

2. Armar Estructura Vistas APP (Cuadro - Base + navBar)
    - base.html
        - navbar
        - footer
        - about
        - contact 
3. Crear los 2 Formularios necesarios de REGISTRO
```bash
 path('register/',views.registerView,name='register_url'), # FORMS
 path('register_tipo/',views.register_tipoView,name='register_tipo_url'), # FORMS
```
4. Crear la vista de PERFIL y el FORM de edit_PERFIL
```bash
 path('view_profile/',views.profile,name='profile'), # No Forms
 path('udpate_profile/',views.profile,name='update_profile'), # FORMS
```

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
```py
# Filtrar todos los inmuebles del userArrendador
path('dashboard_arrendador/',views.dashboardView_arrendador,name='dashboard_arrendador'),
path('new_inmueble/',views.new_inmuebleView,name='new_inmueble'),
path('edit_inmueble/',views.new_inmuebleView,name='edit_inmueble'),
path('list_solicitudes/',views.new_inmuebleView,name='list_solicitudes'),

# Filtrar todos los inmuebles disponibles
path('dashboard_arrendatario/',views.dashboardView_arrendatario,name='dashboard_arrendatario'),
path('crear_solicitud/',views.new_inmuebleView,name='crear_solicitud'),

BTTN para EDITAR INMUEBLE
BTTN para ELIMINAR INMUEBLE
BTTN para cambiar disponibilidad
BTTN para ver Solicitudes

BTTN para enviar Solicitud
```
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
