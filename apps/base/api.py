from rest_framework import generics
class GeneralListApiView(generics.ListAPIView):
    #clases genericas del django restFramework tiene un metodo get_serializer() 
    # que retorna "serializer_class"
    serializer_class = None
    
    #este Retorna lo que esta en una variable queryset
    def get_queryset(self):
      # tomamos el get_serializer() para acceder al Meta donde se asigna el modelo 
      # y se tranforma los datos
      model = self.get_serializer().Meta.model
      return model.objects.filter(state = True) 
        
