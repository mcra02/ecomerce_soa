from datetime import datetime
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from rest_framework.authtoken.views import ObtainAuthToken

from apps.Users.api.serializers.user_serializers import UserTokenSerializer

# Create your views here.
class UserToken(APIView):
    def get(selft,request,*args,**kwargs):
        username = request.GET.get('username')
        try:
            user_token = Token.objects.get(user = self.user)
            user = UserTokenSerializer(self.user)
            return Response({
                'token': user_token.key,
                'user': user.data
            })
        except:
            return Response({
                'error': 'Credenciales enviadas incorrectas.'
            },status = status.HTTP_400_BAD_REQUEST)
            
class Login(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        login_serializer = self.serializer_class(data = request.data, context = {'request': request})
        #print('gaaaaa')
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token,created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                
                if created:
                    return Response({
                        'token': token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesion Exitoso'
                    },status = status.HTTP_201_CREATED)
                else:
                    '''
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key,
                        'user':user_serializer.data,
                        'message':'Inicio de sesion Exitoso'
                    },status = status.HTTP_201_CREATED)
                    '''
                    token.delete()
                    return Response({
                        'error': 'ya se ha iniciado sesion con este usuario'},
                                    status = status.HTTP_409_CONFLICT)
            else:
                return Response({'error': 'Este usuarios No puede iniciar sesion'},
                                status = status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({'error':'Nombre o contraceña de este usuarios son incorrectos o no existe'})
        
        return Response({'mensaje': 'hola desde view response'}, status = status.HTTP_200_OK)
    
class Logout(APIView):
    def get(self, request,*args, **kwargs):
        
        try:
            token = request.GET.get('token')
            print(token)
            token = Token.objects.filter(key = token).first()
            
            if token:
                user = token.user
                all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                if all_sessions.exists():
                    for session in all_sessions:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
                token.delete()
                session_message = 'Sesiones de usuarios eliminados'
                token_message = 'token eliminado'
                return Response({'token_mensage':token_message,'session_mesange':session_message},
                                    status = status.HTTP_200_OK)
            
        except:
            return Response({'error':'No se ah encontrado con esta credenciales .'},
                                    status = status.HTTP_400_BAD_REQUEST)       


                        