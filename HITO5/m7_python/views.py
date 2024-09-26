from django.shortcuts import render, redirect, get_object_or_404
from .services import (get_all_inmuebles, get_or_create_user_profile, get_inmuebles_for_arrendador, 
                       create_inmueble_for_arrendador, actualizar_disponibilidad_inmueble)
from django.contrib.auth.decorators import login_required
from .forms import (CustomUserCreationForm, UserProfileForm, ContactModelForm, UserForm, 
                    UserEditProfileForm, InmuebleForm, EditDisponibilidadForm, 
                    UpdateSolicitudEstadoForm)
from .models import UserProfile, ContactForm, Inmueble, Solicitud, User, Region, Comuna
from django.contrib.auth import login
from django.contrib import messages  # type: ignore
from .decorators import rol_requerido


#* Route para manejo de NOT_AUTH
def not_authorized_view(request):
    return render(request, "not_authorized.html", {})


# Create your views here.

#TODO__ Es buena la idea de pensar esta VIEW como una posible BIFURCACIÓN
#! ES `/` -> es LA VISTA de INICIO de nuestra APP, es la más importante a considerar
@login_required
def indexView(request):
    if request.user.is_authenticated:
        profile = get_or_create_user_profile(request.user)
        if profile.rol == 'arrendador':
            messages.success(request, 'Bienvenido Arrendador')
            return redirect('dashboard_arrendador')
        elif profile.rol == 'arrendatario':
            messages.success(request, 'Bienvenido Arrendatario')
            return redirect('index_arrendatario')
        else: 
            return redirect('login')
        # inmuebles = get_all_inmuebles()
        # return render(request,'index.html',{'inmuebles':inmuebles} )
    else:
        return redirect('login')
    
#_________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

#* FILTROS - SERVICES - SEARCH

def buscar_por_nombre(search_value, inmuebles_list):
    filtered_inmuebles = [inmueble for inmueble in inmuebles_list if search_value.lower() in inmueble.nombre.lower()]
    print('in search')
    return filtered_inmuebles
#! Estas van a ser funciones (services)
#* x REGION y x COMUNA
def filtros_combinados(inmuebles, region='todas', comuna='todas'):
    if region != 'todas':
        inmuebles = inmuebles.filter(comuna__region__nombre=region)
    if comuna != 'todas':
        inmuebles = inmuebles.filter(comuna__nombre=comuna)
    return inmuebles 
 
@login_required 
def index_arrendatario(request):
    inmuebles = get_all_inmuebles()
    
    #* Manejo de si el Inmueble ha sido solicitado o no por el arrendatario
    #* Agregamos al inmueble una nueva prop solicitudes_filtradas
    user = request.user
    for inmueble in inmuebles:
        # Obtener las solicitudes del inmueble que pertenezcan al usuario actual
        inmueble.solicitudes_filtradas = inmueble.solicitudes.filter(arrendatario=user,estado__in=['pendiente', 'aprobada'])
    #*--------------------------------------------------------------------
    
    
    # inmuebles = filtros_combinados(inmuebles, 'De Valparaíso')
    # inmuebles = filtros_combinados(inmuebles, 'De Valparaíso')
    comunas = Comuna.objects.all().order_by('nombre')
    regiones = Region.objects.all().order_by('nombre')
    
    comuna = request.GET.get('comuna', 'todas')
    region = request.GET.get('region', 'todas')
    print(f'-comuna-> {comuna}')
    print(f'-region-> {region}')
    
    
    # if region == 'todas':
    #     comuna = 'todas'
        
    inmuebles = filtros_combinados(inmuebles, region, comuna)
    
    #* SEARCH 
    search_value = request.POST.get('search', '') if request.method == 'POST' else ''
    print(f'search_value -> {search_value}')
    if search_value:
        inmuebles = buscar_por_nombre(search_value, inmuebles)
    
    
    return render(request,'arrendatario/index_arrendatario.html',{'inmuebles':inmuebles, 'comunas':comunas, 'selected_comuna': comuna, 'regiones':regiones, 'selected_region': region} )


@login_required 
def dashboard_arrendador(request):
    inmuebles = get_inmuebles_for_arrendador(request.user)
    return render(request, 'arrendador/dashboard_arrendador.html', {'inmuebles': inmuebles})



# STEP -> CREAR el FORM de Registro
#TODO__ REGISTER and REGISTER_ROL (tipo de usuario) - FORMS
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register_rol')
    else:
        form = CustomUserCreationForm()
    return render(request,'registration/register.html',{'form':form} )

@login_required
def register_rol(request):
    user_profile = get_or_create_user_profile(request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirige a la página de inicio o cualquier otra página
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'registration/register_rol.html', {'form': form})


#* VER PERFIL
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

#* EDITAR PERFIL -> UserForm, UserEditProfileForm
@login_required
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
"""
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono']
"""

# def todas_las_vistas_tienen_el_request(request):
#     request.user 
#     request.user.first_name
#     request.user.last_name 
#     request.user.user_profile.rol
#     pass



#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
# VISTAS SIMPLES 

def about(request):
    return render(request, 'about.html', {})

@login_required
def contact(request):
    if request.method == 'POST':
        form = ContactModelForm(request.POST) # <- {"customer_email": "kiki@gamial.com", "customer_name": "Kiki", "message": "Hola soy Kiki"}
        print(f'errors -> {form.errors}')
        if form.is_valid():
            #* MODEL - Guardamos la data en nuestra DB en la TABLA CONACTFORM
            ContactForm.objects.create(**form.cleaned_data) # pasamos la data del diccionario .cleaned_data a argumentos
            # messages.success(request, f'Gracias por contactarse con nosotros, en breve le responderemos.')
            return redirect('home')
    else: 
        form = ContactModelForm()   
    return render(request, 'contact.html', {'form':form})


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ ARRENDADOR - VIEWS

#* HITO 4

@login_required
@rol_requerido('arrendador')
def create_inmueble(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            inmueble = create_inmueble_for_arrendador(request.user, form.cleaned_data)
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm()
    return render(request, 'arrendador/create_inmueble.html', {'form': form})

@login_required
def edit_inmueble(request, inmueble_id):
    inmueble_edit =  get_object_or_404(Inmueble, id=inmueble_id)
    # inmueble_edit =  Inmueble.objects.get(pk=inmueble_id)
    if request.method == 'POST':
        form = InmuebleForm(request.POST, instance=inmueble_edit)
        if form.is_valid():
            #* Crear service para update Inmueble y validar
            form.save()
            return redirect('dashboard_arrendador')
    else: 
        form = InmuebleForm(instance=inmueble_edit)
    return render(request, 'arrendador/edit_inmueble.html', {'form': form})

#* DAY 17 HITO 4 - VIERNES
@login_required
def delete_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        inmueble.delete()
        return redirect('dashboard_arrendador')

    return render(request, 'arrendador/delete_inmueble.html', {'inmueble': inmueble})


@login_required
def detail_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    
    #* Agrego esto para diferenciar de solicitud ya enviada de no haber enviado a este inmueble
    inmueble.solicitudes_filtradas = inmueble.solicitudes.filter(
            arrendatario=request.user,
            estado__in=['pendiente', 'aprobada']  # Solo solicitudes pendientes o aprobadas
        )
    return render(request, 'detail_inmueble.html', {'inmueble': inmueble})



#* DAY 18 HITO 4 - LUNES
@login_required
def edit_disponibilidad_inmueble(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        form = EditDisponibilidadForm(request.POST, instance=inmueble) 
        if form.is_valid():
            disponible = form.cleaned_data['disponible']
            result = actualizar_disponibilidad_inmueble(inmueble_id, disponible)
            if result["success"]:
                messages.success(request, result["message"])
            else: 
                messages.error(request, result["message"])
            return redirect('dashboard_arrendador')
             
    else: 
        form = EditDisponibilidadForm(instance=inmueble)
    return render(request, 'arrendador/edit_disponibilidad.html', {'form': form, 'inmueble': inmueble})


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ ARRENDATARIOS - VIEWS


@login_required
@rol_requerido('arrendatario')
def send_solicitud(request, inmueble_id):
    inmueble = get_object_or_404(Inmueble, id=inmueble_id)
    if request.method == 'POST':
        solicitud = Solicitud(arrendatario= request.user, inmueble= inmueble, estado= 'pendiente')
        solicitud.save()
        messages.success(request, f'Solicitud inmueble {inmueble.nombre} realizada con éxito!!!')
        return redirect('index_arrendatario')
    return render(request, 'arrendatario/send_solicitud.html', {'inmueble': inmueble})
    
    

def view_list_user_solicitudes(request):
    
    arrendatario =  get_object_or_404(User, id=request.user.id)
    solicitudes = Solicitud.objects.filter(arrendatario=arrendatario)
    return render(request, 'arrendatario/list_user_solicitudes.html', {
        'solicitudes': solicitudes,
        'arrendatario': arrendatario
    })

#*___________________________________________HITO 4 FIN *****************


#* DAY 19 HITO 5 - MARTES

#* del ARRENDADOR
@login_required
def view_list_solicitudes(request, inmueble_id):
    # Obtenemos inmueble para validar previamente
    inmueble = get_object_or_404(Inmueble, id=inmueble_id) 
    solicitudes = Solicitud.objects.filter(inmueble_id=inmueble_id)
    return render(request, 'arrendador/list_solicitudes.html', {'inmueble':inmueble, 'solicitudes': solicitudes})



@login_required
def edit_status_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id) 
    if request.method == 'POST':
        form = UpdateSolicitudEstadoForm(request.POST, instance=solicitud)
        if form.is_valid():
            form.save()
            print(f'--> {form.cleaned_data['estado']}')
            return redirect('view_list_solicitudes', inmueble_id=solicitud.inmueble.id)
    else:
        form = UpdateSolicitudEstadoForm(instance=solicitud) # no la usamos a la data de esta instancia
    return 



@login_required
@rol_requerido('arrendatario')
def cancelar_solicitud(request, solicitud_id):
    solicitud = get_object_or_404(Solicitud, id=solicitud_id)
    inmueble = solicitud.inmueble
    # Eliminar la solicitud solo si está en estado 'pendiente'
    if solicitud.estado == 'pendiente':
        solicitud.delete()
        messages.success(request, f'Solicitud cancelada para el inmueble {inmueble.nombre}')
        return redirect('solicitudes')
    else:
        # Puedes redirigir a una página de error o mostrar un mensaje si el estado no permite la eliminación
        return redirect('solicitudes')


#* del ARRENDATARIO - VER que botón se le puede o debe anexar
#* DAY 20 HITO 5 - LUNES
def detail_inmueble_user(request, inmueble_id):
    pass 



"""
messages {
}

messages se carga desde la VIEW y se consume desde el TEMPLATE (de estar implementado)
"""





#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ EJEMPLO - paso a paso 
#1. simple template - ejemplo.html 
#2. simple vista 

def view_ejemplo_form(request, data_id):
    print(f'id por params --> {data_id}')
    inmu = Inmueble.objects.get(id=data_id)
    print(f'inmu encontrado --> {inmu}')
    
    context = {
        
    }
    return render(request, 'ejemplo.html', context)


