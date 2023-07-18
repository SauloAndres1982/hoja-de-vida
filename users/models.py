from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField('Correo electrónico', unique=True)    
    photo = models.ImageField(verbose_name="Foto de perfil", upload_to='media/img/img1')
    resume = models.TextField(max_length=120)
    city = models.CharField(max_length=120, verbose_name="Ciudad")
    country = models.CharField(max_length=120, verbose_name='Pais')
    recruiter = models.BooleanField(default=False, verbose_name="Reclutador")
    experience = models.BooleanField(default=False, verbose_name="Experiencia")
    created = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, blank=True, verbose_name="Creado")
    modified = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name="Modificado")    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    

    def __str__(self):
        return self.email



# Create your models here.
