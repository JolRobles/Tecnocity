from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.urls import reverse, reverse_lazy
from articulos.models import *
from articulos.forms import *

# Create your views here.
def articulos_list(request):
    articulos = Producto.objects.all()

    context = {
        'articulos':articulos
    }
    return render(request, 'admin/articulos/articulos_list.html', context)

def articulo_create(request):
    form_articulo = ArticuloForm()
    if request.method == 'POST':
        form_articulo = ArticuloForm(request.POST, request.FILES)
        if form_articulo.is_valid():
            form_articulo.save()
            messages.info(request, "El articulo se creo con éxito")
            return redirect('articulos:articulos_list')
        else:
            messages.error(request, articulo.errors)
            context = {
                'form_articulo': form_articulo,
            }
    context = {
        'form_articulo': form_articulo,
    }
    return render(request, 'admin/articulos/articulo_form.html', context)

def articulo_edit(request, pk):
    articulo = Producto.objects.get(pk=pk)
    form_articulo = ArticuloForm(instance = articulo)
    if request.method == 'POST':
        form_articulo = ArticuloForm(request.POST, instance = articulo)
        if form_articulo.is_valid():
            form_articulo.save()
            messages.info(request, "El articulo se editó con éxito")
            return redirect('articulos:articulos_list')
        else:
            messages.error(request, articulo.errors)
            context = {
                'form_articulo': form_articulo,
            }
            return render(request, 'admin/articulos/articulo_form.html', context)

    context = {
        'form_articulo': form_articulo,
    }
    return render(request, 'admin/articulos/articulo_form.html', context)


class ArticuloDetail(DetailView):
    model = Producto
    template_name = 'admin/articulos/articulo_detail.html'

class ArticuloDelete(DeleteView):
    model = Producto
    template_name = 'admin/articulos/articulo_confirm_delete.html'
    success_url = reverse_lazy('articulos:articulos_list')


def marca_create(request):
    form_marca = MarcaForm()
    if request.method == 'POST':
        form_marca = MarcaForm(request.POST, request.FILES)
        if form_marca.is_valid():
            form_marca.save()
            messages.info(request, "La marca se creo con éxito")
            return redirect('articulos:marcas_list')
        else:
            messages.error(request, articulo.errors)
            context = {
                'form_marca': form_marca,
            }
    context = {
        'form_marca': form_marca,
    }
    return render(request, 'admin/articulos/marca_form.html', context)

def marca_edit(request, pk):
    marca = Marca.objects.get(pk=pk)
    form_marca = MarcaForm(instance = marca)
    if request.method == 'POST':
        form_marca = MarcaForm(request.POST, request.FILES, instance = marca)
        if form_marca.is_valid():
            form_marca.save()
            messages.info(request, "La marca se editó con éxito")
            return redirect('articulos:marcas_list')
        else:
            messages.error(request, marca.errors)
            context = {
                'form_marca': form_marca,
            }
            return render(request, 'admin/articulos/marca_form.html', context)

    context = {
        'form_marca': form_marca,
    }
    return render(request, 'admin/articulos/marca_form.html', context)


class MarcaDetail(DetailView):
    model = Marca
    template_name = 'admin/articulos/marca_detail.html'

class MarcaDelete(DeleteView):
    model = Marca
    template_name = 'admin/articulos/marca_confirm_delete.html'
    success_url = reverse_lazy('articulos:marcas_list')

def marcas_list(request):
    marcas = Marca.objects.all()

    context = {
        'marcas':marcas
    }
    return render(request, 'admin/articulos/marcas_list.html', context)

def categoria_create(request):
    form_categoria = CategoriaForm()
    if request.method == 'POST':
        form_categoria = CategoriaForm(request.POST)
        if form_categoria.is_valid():
            form_categoria.save()
            messages.info(request, "El articulo se creo con éxito")
            return redirect('articulos:categorias_list')
        else:
            messages.error(request, articulo.errors)
            context = {
                'form_categoria': form_categoria,
            }
    context = {
        'form_categoria': form_categoria,
    }
    return render(request, 'admin/articulos/categoria_form.html', context)

def categorias_list(request):
    categorias = Categoria.objects.all()

    context = {
        'categorias':categorias
    }
    return render(request, 'admin/articulos/categorias_list.html', context)

def categoria_edit(request, pk):
    categoria = Categoria.objects.get(pk=pk)
    form_categoria = CategoriaForm(instance = categoria)
    if request.method == 'POST':
        form_categoria = CategoriaForm(request.POST,  instance = categoria)
        if form_categoria.is_valid():
            form_categoria.save()
            messages.info(request, "La categoria se editó con éxito")
            return redirect('articulos:categorias_list')
        else:
            messages.error(request, categoria.errors)
            context = {
                'form_categoria': form_categoria,
            }
            return render(request, 'admin/articulos/categoria_form.html', context)

    context = {
        'form_categoria': form_categoria,
    }
    return render(request, 'admin/articulos/categoria_form.html', context)


class CategoriaDetail(DetailView):
    model = Categoria
    template_name = 'admin/articulos/categoria_detail.html'

class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'admin/articulos/categoria_confirm_delete.html'
    success_url = reverse_lazy('articulos:categorias_list')
