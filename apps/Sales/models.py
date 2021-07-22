from django.db import models
from apps.Products.models import Product
from apps.Clients.models import Client
from apps.Users.models import User
from apps.base.models import BaseModel
from simple_history.models import HistoricalRecords
# Create your models here.

class Sale(BaseModel):
    client =  models.ForeignKey(Client,on_delete = models.CASCADE, verbose_name='comprador') 
    user =  models.ForeignKey(User,on_delete = models.CASCADE, verbose_name='vendedor') 
    date_sale =  models.DateTimeField("fecha de venta", auto_now_add=True)
    total_price = models.IntegerField("precio total" , blank = False, null = False)
    historical = HistoricalRecords();
    #registar modificaciones segun usuario
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        verbose_name = "venta"
        verbose_name_plural = "ventas"
    
    def __str__(self):
        return f'{self.id}'


class DetailSale(BaseModel):
    sale = models.ForeignKey(Sale,related_name='detalles',on_delete=models.CASCADE, verbose_name='boleta de de venta')
    product_id =  models.ForeignKey(Product,on_delete = models.CASCADE) 
    cantidad =  models.IntegerField("Cantidad por detalle" , blank = False, null = True)
    precio =  models.IntegerField("Precio del detalle" , blank = False, null = True)
    historical = HistoricalRecords();
    #registar modificaciones segun usuario
    @property
    def _history_user(self):
        return self.changed_by
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    

    class Meta:
        verbose_name = "detalle de ventas"
        verbose_name_plural = "detalles de ventas"

    def __str__(self):
        return f'{self.sale}-venta :  {self.cantidad} {self.product_id}s por el monto de {self.precio} '
