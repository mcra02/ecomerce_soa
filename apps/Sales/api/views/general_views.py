from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from apps.Sales.api.serializers.general_serializers import DetailSaleSerializer

class DetailSaleViewSet(viewsets.ModelViewSet):
    serializer_class = DetailSaleSerializer
    queryset = DetailSaleSerializer.Meta.model.objects.filter(state = True)
    
    def get_query(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active=True).first()
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'detalle agregado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)