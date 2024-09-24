from django.contrib.auth.forms import UserCreationForm
from django import forms # type: ignore
from .models import UserProfile, ContactForm, Inmueble, Solicitud
from django.contrib.auth.models import User

#TODO_ REGISTER - FORM

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido. Ingrese una dirección de correo electrónico válida.')
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Este correo electrónico ya está en uso.")
        return email

#TODO_ REGISTER_ROL - FORM  +  Etapa de Edit PROFILE
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono', 'rol']

#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

#TODO_ EDIT PROFILE -FORM
#* -> UserProfileForm - este form nos va a servir además para cuando vayamos a editar el perfil
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']
class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['rut', 'direccion', 'telefono']
        
#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████

#TODO__ FORM CONTACTO
class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['customer_email', 'customer_name', 'message']
        
#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ FORM INMUEBLE - CREAR 
class InmuebleForm(forms.ModelForm):
    class Meta: 
        model = Inmueble
        fields = [
            'nombre', 'descripcion', 'm2_construidos', 'm2_totales',
            'num_estacionamientos', 'num_habitaciones', 'num_baños',
            'direccion', 'tipo_inmueble', 'precio', 'disponible',
            'comuna'
        ]

#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ FORM SOLICITUDES 
class UpdateSolicitudEstadoForm(forms.ModelForm):
    class Meta:
        model = Solicitud
        fields = ['estado']
        widgets = {
            'estado': forms.Select(choices=Solicitud.ESTADOS)  # ChoiseField basado en el modelo
        } 


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
#TODO__ FORM DISPONIBILIDAD  

class EditDisponibilidadForm(forms.ModelForm):
    class Meta:
        model = Inmueble
        fields = ['disponible']  # Solo permitimos modificar la disponibilidad
        widgets = {
            'disponible': forms.CheckboxInput(),  # Input como checkbox (disponible o no)
        }


#___________________________________________________________________________________________________
#███████████████████████████████████████████████████████████████████████████████████████████████████
# #TODO__ FORM EJEMPLO 
# class EjemploInmuebleForm(forms.ModelForm):
#     class Meta: 
#         model = Inmueble
#         fields = [
#             'nombre', 'descripcion'
#         ]

