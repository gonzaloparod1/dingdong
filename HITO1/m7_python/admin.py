from django.contrib import admin

# Register your models here.
from .models import UserProfile, Inmueble, Comuna, Region
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Inmueble)
admin.site.register(Comuna)
admin.site.register(Region)
