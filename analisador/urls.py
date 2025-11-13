from django.contrib import admin
from django.urls import path, include 
    
# Importa as views do app 'nucleo'
from nucleo import views as nucleo_views

urlpatterns = [
    # URLs do Admin
    path('admin/', admin.site.urls),
    path('nested_admin/', include('nested_admin.urls')),
    
    # URL da Página Principal (Home)
    # Aponta para a view 'home' que criamos
    path('', nucleo_views.home, name='home'),
]