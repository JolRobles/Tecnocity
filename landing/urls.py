from django.urls import path
from . import views


urlpatterns = [
    # The home page
    path(r'', views.index, name='index'),
    path(r'catalogo', views.catalogo, name='catalogo'),
    path(r'nosotros', views.nosotros, name='nosotros'),
    path(r'contacto', views.contacto, name='contacto'),
]
