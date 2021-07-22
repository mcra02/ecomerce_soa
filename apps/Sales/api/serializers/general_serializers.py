from apps.Sales.models import DetailSale
from apps.Sales.models import Sale
#from apps.Sales.api.serializers.sale_serializers import SaleSerializer
from rest_framework import serializers


class DetailSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailSale
        #exclude = ('state','created_date','modified_date','delete_date')
        fields = '__all__'
    
    def to_representation(self,instance):
        print(type(instance))
        return {
            'precio': instance.precio,
            'cantidad': instance.cantidad,
            'sale': instance.sale.id,
            'product_id': instance.product_id.id,
        }
    '''
    def create(self, validated_data):
        venta_data = validated_data.pop('sale')
        detalle_venta = DetailSale.objects.create(**validated_data)
        Sale.objects.create(detalle_venta = detalle_venta, **venta_data)
        return detalle_venta
    '''
        