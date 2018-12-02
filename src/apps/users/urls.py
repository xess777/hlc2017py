from apps.core.routers import AppRouter

from .views import UserViewSet

router = AppRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
