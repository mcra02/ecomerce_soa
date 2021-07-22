from rest_framework import generics
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response


#from apps.base.api import GeneralListApiView
from apps.Users.authentication_mixins import Authentication
from apps.Clients.api.serializers.client_serializers import ClientSerializer

class ClientViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()
    
    def list(self,request):
        client_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(client_serializer.data,status = status.HTTP_200_OK)
    
    def create(self,request):
        client_serializer = self.serializer_class(data = request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response({'message':'Cliente creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(client_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk= None):
        if self.get_queryset(pk):
            client_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
            if client_serializer.is_valid():
                client_serializer.save()
            return Response(client_serializer.data,status = status.HTTP_200_OK)
        return Response(client_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def destroy(self,request,pk=None):
        client = self.get_queryset().filter(id=pk).first()
        if client:
            client.state = False
            client.save()
            return Response({'message':'Cliente Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Cliente con ese id'},status = status.HTTP_400_BAD_REQUEST)
    
'''    
class ClientListAPIView(GeneralListApiView):
    serializer_class = ClientSerializer
     
class ClientCreateAPIView(generics.CreateAPIView):
    serializer_class = ClientSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Cliente creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ClientRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    

class ClientDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
  
    def delete(self,request,pk=None):
        client = self.get_queryset().filter(id=pk).first()
        if client:
            client.state = False
            client.save()
            return Response({'message':'Cliente Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Cliente con ese id'},status = status.HTTP_400_BAD_REQUEST)


class ClientUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ClientSerializer
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id = pk).first()
    
    def patch(self,request,pk = None):
        if self.get_queryset(pk):
            client_serializer= self.serializer_class(self.get_queryset(pk))
            return Response(client_serializer.data,status = status.HTTP_200_OK)
        return Response({'error':'No existeProducto con estos datos!'},status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk=None):
        if self.get_queryset(pk):
            client_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if client_serializer.is_valid():
                client_serializer.save()
                return Response(client_serializer.data,status = status.HTTP_200_OK)
            return Response(client_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
            
'''