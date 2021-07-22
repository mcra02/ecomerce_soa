from apps.Products.models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude = ('state','created_date','modified_date','delete_date')
        
    def to_representation(self,instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'stock': instance.stock,
            'price': instance.price,
            'brand': instance.brand,
            'measure_unit': instance.measure_unit.description
        }