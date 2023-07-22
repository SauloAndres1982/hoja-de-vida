from django.urls import path
from curriculum import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.proyectoDev, name="proyectodev"),
    path("exp", views.experienciaLab, name = "experiencia")
]
