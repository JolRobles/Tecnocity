# Create your views here.
from django.shortcuts import render, redirect
from articulos.models import *
from empresas.models import *
# Create your views here.
def index(request):
    productos = list(reversed(Producto.objects.all()))[:4]
    producto_oferta = Producto.objects.filter(is_oferta=True).last()
    context = {
        'productos': productos,
        'producto_oferta':producto_oferta,
    }

    return render(request, 'app/index.html', context)
def catalogo(request):
    productos = Producto.objects.all()
    categorias = Categoria.objects.all()
    marcas = Marca.objects.all()
    context = {
        'productos': productos,
        'categorias' : categorias,
        'marcas' : marcas,
    }
    return render(request, 'app/products.html', context)

def nosotros(request):
    historias = Historia.objects.all()
    teams = Team.objects.all()
    planes = Plan.objects.all()
    context = {
        'historias':historias,
        'teams':teams,
        'planes':planes,
    }
    # Landing page de cada empresa
    return render(request, 'app/about.html', context)

def contacto(request):
    # Landing page de cada empresa
    return render(request, 'app/contact.html')
