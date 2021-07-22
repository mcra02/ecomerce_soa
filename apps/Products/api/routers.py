from rest_framework.routers import DefaultRouter
from apps.Products.api.views.product_views import ProductViewSet

router = DefaultRouter()
router.register(r'Products',ProductViewSet,basename = 'product')
urlpatterns = router.urls