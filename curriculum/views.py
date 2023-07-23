from django.shortcuts import render, redirect
from curriculum.models import ProyectoDev, ExperienciaLb
from curriculum.forms import ProyectoDevForm

def proyectoDev(request):
    if request.method == 'POST':
        form = ProyectoDevForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("")
    else:
        form = ProyectoDevForm()

    datos_modelo = ProyectoDev.objects.all()
    return render(request, "../templates/curriculum/form_projectsdev.html", {"datos_modelo": datos_modelo, 'form': form})


def experienciaLab(request):
    experiencia = ExperienciaLb.objects.all()
    return render(request, "../templates/curriculum/form_experiencia.html", {"experiencia":experiencia})

# Create your views here.
