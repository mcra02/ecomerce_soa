from apps.Products.models import MeasureUnit
from rest_framework import serializers


class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('state','created_date','modified_date','delete_date')