from django.urls import path
from curriculum.api.views import tecnologias_list, tecnologia_detalle, proyectoDev_list, proyectoDev_detalle
#from curriculum.api.views import TecnologiasListView, TecnologiasDetailView

urlpatterns = [
    path("listTecno/", tecnologias_list, name="tecnologia-list"),
    path("listTecno/<int:pk>", tecnologia_detalle, name="tecnoligia-detalle"),
    path("listProyecto/", proyectoDev_list, name="tecnologia-list"),
    path("listProyecto/<int:pk>", proyectoDev_detalle, name="tecnoligia-detalle")
]
