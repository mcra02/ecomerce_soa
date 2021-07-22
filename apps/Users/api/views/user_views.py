
from rest_framework import viewsets
from rest_framework import status
from apps.Users.models import User
from rest_framework.response import Response
from apps.Users.authentication_mixins import Authentication

from apps.Users.api.serializers.user_serializers import UserSerializer
from apps.Users.api.serializers.user_serializers import UserListSerializer

class UserViewSet(Authentication,viewsets.ModelViewSet):
    serializer_class = UserSerializer
    #queryset = UserSerializer.Meta.model.objects.filter(is_active=True)
    def list(self,request):
        #user_serializer = self.get_serializer(self.get_queryset(),many = True)
        usuarios = User.objects.all().values('id','username','email','password','name').filter(is_active=True)
        user_serializer = UserListSerializer(usuarios, many = True)
        return Response(user_serializer.data,status = status.HTTP_200_OK)
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        return self.get_serializer().Meta.model.objects.filter(id = pk, is_active=True).first()
    
    def create(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        if self.get_queryset(pk):
            
            user_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data, status = status.HTTP_200_OK)
            return Response(user_serializer.errors,status = status.HTTP_400_BAD_REQUEST)
         
    def destroy(self,request,pk=None):
        usuario = self.get_queryset().filter(id = pk).first()
        if usuario:
            usuario.is_active = False
            usuario.save()
            return Response({'message':'Usuario Eliminado correctamente'}, status = status.HTTP_200_OK)
        return Resquest({'error':'No existe usuario con esa informacion'}, status = status.HTTP_400_BAD_REQUEST)    
    '''
    def post(self,request):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Usuario creado correctamente!'},status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status= status.HTTP_400_BAD_REQUEST)
     '''
        
        