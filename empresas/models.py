from django.db import models

# Create your models here.
class Historia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    imagen = models.ImageField(upload_to='static/admin/images/empresa', help_text='Escoja una imagen referencial a la historia')


    class Meta:
        verbose_name = "Historia"
        verbose_name_plural = "Historias"

    def __str__(self):
        return self.titulo

class Team(models.Model):
    nombre = models.CharField(max_length=100)
    cargo_ocupado = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to='static/admin/images/empresa', help_text='Escoja una imagen referencial a al personaje del equipo')
    descripción = models.CharField(max_length=200)


    class Meta:
        verbose_name = "Team"
        verbose_name_plural = "Teams"

    def __str__(self):
        return self.nombre

class Plan(models.Model):
    TIPO = [
    ('1', 'MISION'),
    ('2', 'VISION'),
    ('3', 'VALORES'),
    ]
    tipo = models.CharField(max_length = 50, choices = TIPO, default='1')
    imagen = models.ImageField(upload_to='static/admin/images/empresa', help_text='Escoja una imagen referencial al tipo de plan estratégico')
    descripcion = models.TextField()


    class Meta:
        verbose_name = "plan"
        verbose_name_plural = "planes"

    def __str__(self):
        return self.descripcion

class Contactos(models.Model):
    ubicacion = models.CharField(max_length=200)
    facebook = models.URLField(blank=True, null=True, help_text='Dirección de facebook de la empresa')
    instagram = models.URLField(blank=True, null=True, help_text='Dirección de instrgram de la empresa')
    twitter = models.URLField(blank=True, null=True, help_text='Dirección de twitter de la empresa')

    class Meta:
        verbose_name = "contactos"
        verbose_name_plural = "contactos"

    def __str__(self):
        return self.ubicacion

class PreguntaFrecuente(models.Model):
    pregunta = models.CharField(max_length=500)
    respuesta = models.CharField(max_length=500)
    class Meta:
        verbose_name = "PreguntaFrecuente"
        verbose_name_plural = "PreguntasFrecuentes"

    def __str__(self):
        return self.pregunta
