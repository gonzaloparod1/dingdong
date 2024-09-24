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
5. Vistas por adelantar
    - home - Index -> 3 posibilidades   1 (form login + register) 2 Arrendador 3 Arrendatario
    - dashboard_arrendador (filter diferenciado de lista de inmuebles)
    - dashboard_arrendatario  (filter diferenciado de lista de inmuebles)

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


```py
#* HITO 4

@login_required
@rol_requerido('arrendador')
def create_inmueble(request):
    pass

@login_required
def edit_inmueble(request, inmueble_id):
    pass

@login_required
def delete_inmueble(request, inmueble_id):
    pass 

@login_required
def detail_inmueble(request, inmueble_id):
    pass

@login_required
def edit_disponibilidad_inmueble(request, inmueble_id):
    pass 

@login_required
def view_list_solicitudes(request, inmueble_id):
    pass 

#*___________________________________________HITO 4 FIN *****************
```

## HITO 5
1. Descripción general del sitio web - completar Doc en README
2. Características base del sitio web - completar Doc en README
3. Problemas o dificultades con los que se encontraron a la hora de desarrollar el sitio web.

4. Presentar puntos de los requerimientos del Hito 4
5. Presentar el filtrado de los inmuebles por comuna y región. - `Nuevas funcionalidades`
6. Ejecutar servidor y demostrar funcionalidad del sitio web a los otros estudiantes.

¡Mucho éxito!!!

---

---

---

---

---

## HITO 3 - PERFIL -> VER 
### Paso a paso 
**Partir de la Idea de que tenemos los MOdels necesarios**

```py
from django.contrib.auth.models import User

class UserProfile(models.Model):
    ROLES = (('arrendador', 'Arrendador'), ('arrendatario', 'Arrendatario'))
    user = models.OneToOneField(User, related_name='user_profile', on_delete=models.CASCADE)
    rut = models.CharField(max_length=9, unique=True)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, null=True, blank=True)
    rol = models.CharField(max_length=255, choices=ROLES, default='arrendatario')
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} ({self.rol})'

```

1. Crear en `forms.py` ambos formularios destacando los campos que nos solicitan EDITAR

    - Nos piden editar: first_name, last_name, email, rut, direccion, telefono 

```py
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono']
```

2. Armar el `profile_detail.html`
    - Determinar que datos vamos a mostrar y armar el template
```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Información Personal</h5>
            <p class="card-text"><strong>Username:</strong> {{ user.username }}</p>
        </div>
    </div>
</div>
{% endblock %}
```
3. Crear la view de `profile_view` 

```py
def profile_view(request):
    user = request.user
    # user_profile = UserProfile.objects.get(user=user)  # Llama al servicio para obtener o crear el perfil
    return render(request, 'profile_detail.html', {
        'user': user,
        # 'profile': user_profile,
    })
```

4. Armar su PATH 
```py
path('profile', profile_view, name='profile'),
```

5. Lo pruebo 
```bash
python manage.py runserver 
```
6. Me voy a `/profile`

7. En caso de ERROR 
    - Ver
    - Entender
    - Solucionar 

8. Armar completo `profile_detail.html`
```html
{% extends 'base.html' %}

{% block content %}
<div class="container mt-5">
    <div class="card">
        <div class="card-body">
            <h5 class="card-title">Información Personal</h5>
            <p class="card-text"><strong>Username:</strong> {{ user.username }}</p>
            <p class="card-text"><strong>Email:</strong> {{ user.email }}</p>
            <p class="card-text"><strong>Nombre:</strong> {{ user.first_name }}</p>
            <p class="card-text"><strong>Apellido:</strong> {{ user.last_name }}</p>
            <p class="card-text"><strong>RUT:</strong> {{ profile.rut }}</p>
            <p class="card-text"><strong>Dirección:</strong> {{ profile.direccion }}</p>
            <p class="card-text"><strong>Teléfono:</strong> {{ profile.telefono }}</p>
            <p class="card-text"><strong>Tipo de usuario:</strong> {{ profile.rol | upper }}</p>
            <a href="{% url 'edit_profile' %}" class="btn btn-primary mt-3">Editar Perfil</a>
        </div>
    </div>
</div>
{% endblock %}
```
9. Crear toda la view de `profile_view` y sus services de ser necesarios

```py
@login_required
def profile_view(request):
    user = request.user
    user_profile = get_or_create_user_profile(user)  # Llama al servicio para obtener o crear el perfil

    if not user_profile:
        # En caso de que ocurra un error al obtener o crear el perfil
        return render(request, 'error.html', {'message': 'No se pudo obtener el perfil del usuario.'})

    return render(request, 'profile_detail.html', {
        'user': user,
        'profile': user_profile,
    })
```

10. Implementar su referencia, bttn que nos va a llevar a esta vista 
```py
<a class="nav-link" href="{% url 'profile' %}">
    <p>
        Bienvenido <strong>{{ user.username }}</strong> 
    </p>
</a>
```
11. Testear

## HITO 3 - PERFIL -> EDITAR 
### Paso a paso 
**Partir de la Idea de que tenemos los Models necesarios**

1. Partir de la idea que ya tenemos vista del perfil
2. Tenemos los forms para ver perfil User los cuales los vamos a re-utilizar
```py
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono']
```
## 1° Ir solamente por el GET (en el caso de los formularios)
3. Armar un html (template) simple pensando en el modelo que vamos a trabajar 
4. Creo la view (la función) con poca info solamente de ser necesario y que renderice dicho template 
5. Crear la urls
6. Testear, ejemplo: pegamos el path
```bash
http://127.0.0.1:8000/profile/edit/
```
7. Crear la vista y el template ya con todos los campos necesarios 
8. Testear
9. De ser necesario modularizamos y creamos services (Manager)
10. Testear 

## 2° Ir por el POST (en el caso de los formularios)

```py
if request.method == 'POST':
```
**Activar nuestra DB**
**Revisar los Modelos - para ser coherentes en nuestro manejo de datos**
**Revisar los FORMS en relación al manejo de campos solicitados**
11. Repetir los pasos del GET pero ya desde el POST
12. Enjoy!!!

---

---

---

---

---



# FLOW app CLIENT 

1. En el navegador se crea http://127.0.0.1:8000/profile/edit/ 
2. Busca el dominio http://127.0.0.1:8000 (localhost) 
3. Accede al SERVIDOR DJANGO
4. Desde el setting.py del project se le indica ir a `ROOT_URLCONF = 'mysite.urls'`
5. En el urls.py del project tenemos:
```py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('m7_python.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
]
```
6. `path('', include('m7_python.urls'))` equivale a:
```py
urlpatterns = [
    path('', indexView, name='home'),
    
    path('accounts/register', register, name='register'),
    path('accounts/register_rol', register_rol, name='register_rol'),
    
    path('profile', profile_view, name='profile'),
    path('profile/edit/', edit_profile_view, name='edit_profile'),
    #____________________________________________________________________
    # PATH (routes) SIMPLES 
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
]
```
Va match (verifica sean idénticas) /profile/edit/ 
7. Si encuentra el indéntico PATH `path('profile/edit/', edit_profile_view, name='edit_profile')` ejecuta la función (view) que le pasamos por 2° params

8. Ejecuta ->
```py
def edit_profile_view(request):
    user = request.user 
    user_profile = get_or_create_user_profile(user)
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserEditProfileForm(request.POST, instance=user_profile) 
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    else: # GET
        user_form = UserForm(instance=user) 
        profile_form = UserEditProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
```
9. Esta función pregunta si es método es GET o POST
10. En primera instancia si entramos a esta vista SIN el submit es de tipo GET
```py
    else: # GET
        user_form = UserForm(instance=user) 
        profile_form = UserEditProfileForm(instance=user_profile)
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
```
Con los dos forms que usamos se crea un form con la data que ya tenía en este caso el user
11. Acá sucede lo que retorna la función 
```py
    return render(request, 'profile_edit.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })
```
Vemos que en este caso como en la mayoría se renderiza un template `profile_edit.html`




---


---


---


# EXTRA EXTRA BUENAS PRÁCTICAS 

- Crear class Arrendador 
- Crear class Arrendatario 
- Ver el decorator @rol_requerido
- Implementar carga y save real en la db