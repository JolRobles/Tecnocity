from django.urls import path
from . import views


urlpatterns = [
    # The home page
    # path(r'', views.index, name='index'),
    # Articulos
    path(r'articulo_create', views.articulo_create, name='articulo_create'),
    path(r'articulos_list', views.articulos_list, name='articulos_list'),
    path(r'articulo_edit/<int:pk>/', views.articulo_edit, name = 'articulo_edit'),
    path(r'articulo_detail/<int:pk>/', views.ArticuloDetail.as_view(), name = 'articulo_detail'),
	path(r'articulo_delete/<int:pk>/delete/', views.ArticuloDelete.as_view(), name='articulo_delete'),

    # categorias
    path(r'categoria_create', views.categoria_create, name='categoria_create'),
    path(r'categorias_list', views.categorias_list, name='categorias_list'),
    path(r'categoria_edit/<int:pk>/', views.categoria_edit, name = 'categoria_edit'),
    path(r'categoria_detail/<int:pk>/', views.CategoriaDetail.as_view(), name = 'categoria_detail'),
	path(r'categoria_delete/<int:pk>/delete/', views.CategoriaDelete.as_view(), name='categoria_delete'),

    # marcas
    path(r'marca_create', views.marca_create, name='marca_create'),
    path(r'marcas_list', views.marcas_list, name='marcas_list'),
    path(r'marca_edit/<int:pk>/', views.marca_edit, name = 'marca_edit'),
    path(r'marca_detail/<int:pk>/', views.MarcaDetail.as_view(), name = 'marca_detail'),
	path(r'marca_delete/<int:pk>/delete/', views.MarcaDelete.as_view(), name='marca_delete'),
]
