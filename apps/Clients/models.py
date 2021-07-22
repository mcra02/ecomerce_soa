from django.db import models
from simple_history.models import HistoricalRecords
from apps.base.models import BaseModel

# Create your models here.
class  Client(BaseModel):  
    dni = models.CharField("dni usuario",max_length=200, blank = False, null = True)  
    name = models.CharField("nombre usuario",max_length=200, blank = True, null = False)  
    last_name = models.CharField("apellido usuario",max_length=200, blank = True, null = False)  
    direction = models.CharField("descripcion direccion" ,max_length=200)
    historical = HistoricalRecords();
    
    #registar modificaciones segun usuario
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
        
    class Meta:
        verbose_name ="cliente"
        verbose_name_plural ="clientes"

    def __str__(self):
        return self.name