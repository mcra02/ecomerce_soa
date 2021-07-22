from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response


from apps.base.api import GeneralListApiView
from apps.Users.authentication_mixins import Authentication
from apps.Products.api.serializers.product_serializers import ProductSerializer


class ProductViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = ProductSerializer


    def list(self,request):
        product_serializer = self.get_serializer(self.get_queryset(), many = True)
        return Response(product_serializer.data,status = status.HTTP_200_OK)
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        return self.get_serializer().Meta.model.objects.filter(id = pk,state = True).first()
    
    def create(self,request):
        product_serializer = self.serializer_class(data = request.data)
        if product_serializer.is_valid():
            product_serializer.save()
            return Response({'message':'Producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk= None):
        if self.get_queryset(pk):
            product_serializer= self.serializer_class(self.get_queryset(pk), data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response(client_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
        
    def destroy(self,request,pk=None):
        product_serializer = self.get_queryset().filter(id=pk).first()
        if product_serializer:
            product_serializer.state = False
            product_serializer.save()
            return Response({'message':'Producto Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un Producto con ese id'},status = status.HTTP_400_BAD_REQUEST)
     
    
    
'''
class ProductListAPIView(GeneralListApiView):
    serializer_class = ProductSerializer
     
class ProductCreateAPIView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'producto creado correctamente!'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
    

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state=True)
  
    def delete(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message':'producto Eliminado correctamente!'}, status = status.HTTP_200_OK)
        return Response({'error':'No existe un producto con este id'},status = status.HTTP_400_BAD_REQUEST)


class ProductUpdateAPIView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self,pk):
        return self.get_serializer().Meta.model.objects.filter(state=True).filter(id = pk).first()
    
    def patch(self,request,pk = None):
        if self.get_queryset(pk):
            product_serializer= self.serializer_class(self.get_queryset(pk))
            return Response(product_serializer.data,status = status.HTTP_200_OK)
        return Response({'error':'No existeProducto con estos datos!'},status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request,pk=None):
        if self.get_queryset(pk):
            product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if product_serializer.is_valid():
                product_serializer.save()
                return Response(product_serializer.data,status = status.HTTP_200_OK)
            return Response(product_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
    
'''