from rest_framework.response import Response
from rest_framework.views import APIView
from apps.Users.models import User
from apps.Users.api.serializers import UserSerializer

class UserAPIView(APIView):
    
    def get(self,request):
        # trae a todos los usuarios
        Users =User.objects.all()
        # contiene la infomacion de la 
        # consulta ya serializada
        user_serializer = UserSerializer(Users, many= True)
        return Response(user_serializer.data)
        