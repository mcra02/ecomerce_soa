from apps.Clients.models import Client
from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('state','created_date','modified_date','delete_date')
        
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'dni': instance.dni,
            'name': instance.name,
            'last_name': instance.last_name,
            'direction': instance.direction,
        }
