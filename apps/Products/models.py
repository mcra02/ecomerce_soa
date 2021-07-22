from django.db import models
from simple_history.models import HistoricalRecords

from apps.base.models import BaseModel
# Create your models here.

class MeasureUnit(BaseModel):
    description= models.CharField("Descripcion", max_length=200, blank = False, null = False, unique = True)
    historical = HistoricalRecords();
    #registar modificaciones segun usuario
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'
    def __str__(self):
        return self.description
    
    
class Product(BaseModel):
    name = models.CharField("nombre del producto" ,max_length=200, blank = False, null = False)
    stock = models.IntegerField(default=0 ,blank = False, null = False)
    price = models.IntegerField(default=0 ,blank = False, null = False)
    brand = models.CharField("marca del producto" ,max_length=200, blank = False, null = True, default="desconocido")
    measure_unit = models.ForeignKey(MeasureUnit, on_delete=models.CASCADE, verbose_name='Unidad de Medida', null=True)
    type  = models.CharField("tipo de producto" ,max_length=200, blank = False, null = True, default="desconocido")
    historical = HistoricalRecords();
    
    
    #registar modificaciones segun usuario
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __str__(self):
        return self.name
    