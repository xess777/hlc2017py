from apps.core.routers import AppRouter
from apps.users.views import UserViewSet

router = AppRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls
