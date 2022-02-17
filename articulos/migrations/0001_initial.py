# Generated by Django 4.0.2 on 2022-02-17 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('img_marca', models.ImageField(blank=True, help_text='Escoja una imagen de la marca', null=True, upload_to='static/admin/images/marcas')),
            ],
            options={
                'verbose_name': 'Marca',
                'verbose_name_plural': 'Marcas',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('img_producto', models.ImageField(blank=True, help_text='Escoja una imagen del producto', null=True, upload_to='static/admin/images/products')),
                ('descripcion', models.CharField(max_length=100)),
                ('caracteristicas', models.TextField()),
                ('precio_compra', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('pvp', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('stock', models.IntegerField(blank=True, null=True)),
                ('vendido', models.IntegerField(blank=True, default=0, null=True)),
                ('is_oferta', models.BooleanField(default=False)),
                ('is_nuevo', models.BooleanField(default=True)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articulos.marca')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
            },
        ),
    ]
