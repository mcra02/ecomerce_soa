from apps.Sales.models import Sale,DetailSale
from apps.Sales.api.serializers.general_serializers import DetailSaleSerializer
from rest_framework import serializers

from apps.Products.api.views.product_views import ProductViewSet

class SaleSerializer(serializers.ModelSerializer):
    detalles = DetailSaleSerializer(many = True)
    class Meta:
        model = Sale
        #exclude = ('state','created_date','modified_date','delete_date')
        #fields = ['id','client','user','date_sale','total_price','detalle']
        fields = '__all__'
    '''
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'client': instance.client.name,
            'user': instance.user.name,
            'date_sale': instance.date_sale,
            'total_price': instance.total_price,
            'detalles': detalles,
        }
    '''    
        
    def create(self, validated_data):
        detalles_venta = validated_data.pop('detalles')
        print(detalles_venta)
        sale = Sale.objects.create(**validated_data)
        print(sale)
        for detalle_venta_data in detalles_venta:
            print('----------------------')
            print(detalle_venta_data)
            producto = ProductViewSet.get_queryset(detalle_venta_data['product_id'])
            #print(producto)
            #DetailSale.objects.create(sale=sale, **detalle_venta_data)
            
            DetailSale.objects.create(sale=sale, cantidad=detalle_venta_data['cantidad'], precio=detalle_venta_data['precio'], product_id=detalle_venta_data['product_id']) #**detalle_venta_data)
        return sale