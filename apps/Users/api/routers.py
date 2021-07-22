from rest_framework.routers import DefaultRouter
from apps.Users.api.views.user_views import UserViewSet

router = DefaultRouter()
router.register(r'Users',UserViewSet,basename = 'users')


urlpatterns = router.urls