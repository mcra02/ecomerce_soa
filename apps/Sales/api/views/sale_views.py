from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from apps.base.api import GeneralListApiView
from apps.Sales.api.serializers.sale_serializers import SaleSerializer
#from apps.Sales.api.serializers.general_serializers import DetailSaleSerializer


class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    queryset = SaleSerializer.Meta.model.objects.filter(state = True)
    
    def get_query(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active=True).first()
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        
        #print("dato {} ->".format(serializer))
        if serializer.is_valid():
            #print(serializer.data)
            serializer.save()
            
            return Response({'message': 'venta registrada correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        sale_serializer = self.get_queryset().filter(id=pk).first()
        if sale_serializer:
            sale_serializer.state = False
            sale_serializer.save()
            return Response({'message':'Producto Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con ese id'},status = status.HTTP_400_BAD_REQUEST)