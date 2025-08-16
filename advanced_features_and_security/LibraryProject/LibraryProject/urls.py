from django.contrib import admin
from django.urls import path, include  # Ajout de 'include'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('bookshelf.urls')), # Ajout de la ligne pour inclure les URLs de l'app bookshelf
]