from apps.Sales.models import Sale, DetailSale
from apps.Sales.api.serializers.general_serializers import DetailSaleSerializer
from apps.Products.api.serializers.product_serializers import ProductSerializer
from rest_framework import serializers

from apps.Products.api.views.product_views import ProductViewSet


class SaleSerializer(serializers.ModelSerializer):
    detalles = DetailSaleSerializer(many=True)

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


    def suma_total(self, detalles_venta):
        cant =0
        acumulador = 0
        for detalle_venta_data in detalles_venta:
            for k, v in detalle_venta_data.items():
                if k == 'cantidad':
                    cant = v
                break
                
            print(detalle_venta_data)
            item_n =self.id_producto(detalle_venta_data)
            print('precio producto total+++++++++++++++++++')
            print(cant)
            print(item_n)
            acumulador = item_n*cant + acumulador
        return acumulador
    def id_producto(self, detalles_venta):
        memoria = ''
        for k, v in detalles_venta.items():
            if k == 'product_id':
                memoria = v
                break
        producto =ProductSerializer().Meta.model.objects.filter(name = memoria).first()
        return producto.price

    def create(self, validated_data):
        detalles_venta = validated_data.pop('detalles')
        print(detalles_venta)
        print(
            '-----------------------------------------------------------------------------')
        suma_total_venta = self.suma_total(detalles_venta)
        print('precio total venta ************************')
        print(suma_total_venta)
        sale = Sale.objects.create(state=validated_data['state'],client=validated_data['client'], user=validated_data['user'], total_price=suma_total_venta)
        #sale = Sale.objects.create(**validated_data)
        print(sale)
        for detalle_venta_data in detalles_venta:
            print('imprimineto porducto')
            precio_detalle =self.id_producto(detalle_venta_data)*detalle_venta_data['cantidad']
            print(precio_detalle)
            DetailSale.objects.create(sale=sale, cantidad=detalle_venta_data['cantidad'], precio=precio_detalle
                                      , product_id=detalle_venta_data['product_id'])  # **detalle_venta_data)
        #sale = Sale.objects.create(**validated_data)
        #sale = Sale.objects.create(**validated_data)
        return sale
