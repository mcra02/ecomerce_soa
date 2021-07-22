from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response

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
    def get_queryset(self):
        return MeasureUnit.objects.filter(state=True)
'''   
class MeasureUnitViewSet(viewsets.ModelViewSet):
    serializer_class = MeasureUnitSerializer


    def list(self,request):
        detail_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(detail_serializer.data,status = status.HTTP_200_OK)
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()
    
    def create(self,request):
        detail_serializer = self.serializer_class(data = request.data)
        if detail_serializer.is_valid():
            detail_serializer.save()
            return Response({'message':'Producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(detail_serializer.errors,status = status.HTTP_400_BAD_REQUEST)    
'''


    
    