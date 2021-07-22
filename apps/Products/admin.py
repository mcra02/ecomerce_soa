from django.contrib import admin

# Register your models here.
from apps.Products.models import MeasureUnit,Product
# Register your models here.
admin.site.register(MeasureUnit)
admin.site.register(Product)