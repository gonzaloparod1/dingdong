from django.contrib import admin
from m7_python.models import UserProfile, Inmueble, Comuna, Region, ContactForm, Solicitud


class UserProfileAdmin(admin.ModelAdmin):
    pass

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(Region)
admin.site.register(ContactForm)
admin.site.register(Solicitud)