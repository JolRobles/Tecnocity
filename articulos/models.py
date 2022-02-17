from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.nombre



class Marca(models.Model):
    nombre = models.CharField(max_length=50)
    img_marca = models.ImageField(upload_to='static/admin/images/marcas', help_text='Escoja una imagen de la marca', blank = True, null=True)

    class Meta:
        verbose_name = "Marca"
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    img_producto = models.ImageField(upload_to='static/admin/images/products', help_text='Escoja una imagen del producto', blank = True, null=True)
    descripcion = models.CharField(max_length = 100)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    caracteristicas = models.TextField()
    precio_compra = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    pvp = models.DecimalField(max_digits=6, decimal_places=2, blank = True, null=True)
    stock = models.IntegerField(blank = True, null=True)
    vendido = models.IntegerField(default=0, blank = True, null=True)
    is_oferta = models.BooleanField(default=False)
    is_nuevo = models.BooleanField(default=True)
    activo = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"


    def __str__(self):
        return self.nombre
