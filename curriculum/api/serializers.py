from rest_framework import serializers
from curriculum.models import Tecnologias, ProyectoDev
from users.models import User

class TecnologiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tecnologias
        fields = ['id','nombre_tecnologia']
    #id = serializers.IntegerField(read_only=True)
    #nombre_tecnologia = serializers.CharField()

    
    
class ProyectoDevSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProyectoDev
        fields = ['name', 'url', 'tecnology', 'description', 'id_user', 'created', 'modified']

    tecnology = serializers.PrimaryKeyRelatedField(many=True, queryset=Tecnologias.objects.all())
    id_user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())