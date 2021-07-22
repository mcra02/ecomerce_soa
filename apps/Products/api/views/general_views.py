from rest_framework import generics

# vamos a remplazar 
#from apps.Products.models import MeasureUnit
# por
from apps.base.api import GeneralListApiView

from apps.Products.api.serializers.general_serializers import MeasureUnitSerializer

#trbajo de vistas con metodos  tipo listView -> listas de objetos
# ademas lisAPIView esta hecho para reconocer solo el metodo GET
class MeasureUnitListAPIView(GeneralListApiView): 
    #es necesario crear un objeto tipo serializador el 
    #verificar que el nombre del objeto del serializador se especificamente el "serializer_class"
    serializer_class = MeasureUnitSerializer
    
    #
    #se realiza la consulta. esta busca al serializar para especificado
    # ademas el metodo valida la cantidad valores de llegada
    
    # se remplazara  generics.ListAPIView--> por 
    '''
    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)
    '''
    

