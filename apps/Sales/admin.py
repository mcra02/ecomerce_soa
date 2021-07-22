from django.contrib import admin


from apps.Sales.models import DetailSale,Sale
# Register your models here.
admin.site.register(DetailSale)
admin.site.register(Sale)