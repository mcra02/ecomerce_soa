from rest_framework.routers import DefaultRouter
from apps.Sales.api.views.sale_views import SaleViewSet
from apps.Sales.api.views.general_views import DetailSaleViewSet

router = DefaultRouter()

router.register(r'Sales',SaleViewSet)
router.register(r'DetailSales',DetailSaleViewSet)

urlpatterns = router.urls