from django.contrib import admin

# Register your models here.
from TestApp.models import Usuarios,Eventos,Inscripciones
admin.site.register(Usuarios)
admin.site.register(Eventos)
admin.site.register(Inscripciones)