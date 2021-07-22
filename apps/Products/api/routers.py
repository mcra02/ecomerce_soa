from rest_framework.routers import DefaultRouter
from apps.Products.api.views.product_views import ProductViewSet
#from apps.Products.api.views.general_views import MeasureUnitViewSet

router = DefaultRouter()
router.register(r'Products',ProductViewSet,basename = 'product')
#router.register(r'MeasureUnit',MeasureUnitViewSet,basename = 'unit')
urlpatterns = router.urls