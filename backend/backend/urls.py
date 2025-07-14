#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/', include('users.urls')),  # Todas las rutas de users van aquí con prefijo 'api/'
#]

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect  # 👈 Importa redirect

urlpatterns = [
    path('', lambda request: redirect('/admin/')),  # 👈 Redirección rápida
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),  # Asegúrate de tener este archivo
]
