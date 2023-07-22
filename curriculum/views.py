from django.shortcuts import render
from curriculum.models import ProyectoDev, ExperienciaLb

def proyectoDev(request):
    proyectos = ProyectoDev.objects.all()
    return render(request, "../templates/curriculum/form_projectsdev.html",{"proyectos":proyectos})

def experienciaLab(request):
    experiencia = ExperienciaLb.objects.all()
    return render(request, "../templates/curriculum/form_experiencia.html", {"experiencia":experiencia})

# Create your views here.
