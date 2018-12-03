from apps.core.routers import AppRouter

from .views import LocationViewSet

router = AppRouter()
router.register(r'locations', LocationViewSet)

urlpatterns = router.urls
