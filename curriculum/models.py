from django.db import models
from users.models import User
from .choice import estudios

class Tecnologias(models.Model):
    nombre_tecnologia = models.CharField(verbose_name="Nombre de Tecnología", max_length=50)

    class Meta:
        verbose_name = 'Tecnologia'
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nombre_tecnologia

class ProyectoDev(models.Model):
    name = models.CharField(max_length=120, verbose_name="Nombre de proyecto")
    url = models.URLField(verbose_name="Link del proyecto", max_length=100)
    tecnology = models.ManyToManyField(Tecnologias)
    description = models.TextField(verbose_name="descripcion")
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Modificado")    
    USERNAME_FIELD = "email"

    class Meta:
        verbose_name = "Proyecto desarrollado"
        verbose_name_plural = "Proyectos desarrollados"

    def __str__(self):
        return f'{self.name} {self.url}'
        

class ExperienciaLb(models.Model):

    experiencia = models.BooleanField(default=False)
    empresa = models.CharField(max_length=120)
    cargo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=300)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    def __str__(self):
        return self.cargo
    
class Estudios(models.Model):
    estudio = models.CharField(verbose_name="Estudios", max_length=120, choices=estudios)
    titulo = models.CharField(verbose_name="Título", max_length=120)
    institucion = models.CharField(verbose_name="Institución", max_length=120)
    description = models.TextField(max_length=300, verbose_name="Descripción")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name="Estudio"
        verbose_name_plural="Estudios"

    def __str__(self):
        return self.titulo
    

class Extras(models.Model):
    extra = models.TextField(verbose_name="Extras, hobbies y demás", max_length=400)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name="Extra"
        verbose_name_plural="Extras"

    def __str__(self):
        return self.extra
    
class Habilidades(models.Model):

    habilidad = models.CharField(max_length=200)
    nivel =  models.CharField(max_length=120)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Creado")
    updated = models.DateTimeField(auto_now=True, verbose_name="actualizado")

    class Meta:
        verbose_name="habilidad"
        verbose_name_plural="habilidades"

    def __str__(self):
        return self.habilidad