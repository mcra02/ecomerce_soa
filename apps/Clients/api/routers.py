from rest_framework.routers import DefaultRouter
from apps.Clients.api.views.client_views import ClientViewSet

router = DefaultRouter()
router.register(r'Clients',ClientViewSet,basename = 'client')
urlpatterns = router.urls