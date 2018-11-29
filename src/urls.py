from rest_framework import routers

from apps.users.views import UserViewSet

router = routers.SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = router.urls
