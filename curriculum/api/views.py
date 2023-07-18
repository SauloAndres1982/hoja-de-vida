from curriculum.models import Estudios, Tecnologias, ProyectoDev
from curriculum.api.serializers import TecnologiasSerializer, ProyectoDevSerializer

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

    # class TecnologiasListView(generics.ListAPIView):
    #     queryset = Tecnologias.objects.all()
    #     serializer_class = TecnologiasSerializer

    # class TecnologiasDetailView(generics.RetrieveAPIView):
    #     queryset = Tecnologias.objects.all()
    #     serializer_class = TecnologiasSerializer









@api_view(['GET', 'POST'])
def tecnologias_list(request):
    if request.method=='GET':

        tecnologias = Tecnologias.objects.all()
        serializer = TecnologiasSerializer(tecnologias, many=True) 
        return Response(serializer.data)
    
    if request.method=='POST':
        de_serializer = TecnologiasSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return(de_serializer.errors)
        
@api_view(['GET', 'PUT', 'DELETE'])
def tecnologia_detalle(request, pk):

    if request.method == 'GET':

        tecnologia = Tecnologias.objects.get(pk=pk)
        serializer = TecnologiasSerializer(tecnologia) 
        return Response(serializer.data)

    if request.method == 'PUT':
        tecnologia = Tecnologias.objects.get(pk=pk)
        de_serializer = TecnologiasSerializer(tecnologia, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return(de_serializer.errors)
        
    if request.method == 'DELETE':
        tecnologia = Tecnologias.objects.get(pk=pk)
        tecnologia.delete()
        data = {
            "resultado": True
        }
        return Response(data)
    
    
@api_view(['GET', 'POST'])
def proyectoDev_list(request):
    if request.method=='GET':

        proyectosDev = ProyectoDev.objects.all()
        serializer = ProyectoDevSerializer(proyectosDev, many=True) 
        return Response(serializer.data)
    
    if request.method=='POST':
        de_serializer = ProyectoDevSerializer(data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return(de_serializer.errors)
        
@api_view(['GET', 'PUT', 'DELETE'])
def proyectoDev_detalle(request, pk):

    if request.method == 'GET':

        proyectoDev = ProyectoDev.objects.get(pk=pk)
        serializer = ProyectoDevSerializer(proyectoDev) 
        return Response(serializer.data)

    if request.method == 'PUT':
        proyectoDev = ProyectoDev.objects.get(pk=pk)
        de_serializer = ProyectoDevSerializer(proyectoDev, data=request.data)
        if de_serializer.is_valid():
            de_serializer.save()
            return Response(de_serializer.data)
        else:
            return(de_serializer.errors)
        
    if request.method == 'DELETE':
        proyectoDev = ProyectoDev.objects.get(pk=pk)
        proyectoDev.delete()
        data = {
            "resultado": True
        }
        return Response(data)

