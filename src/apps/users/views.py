from apps.core.viewsets import AppModelViewSet

from .models import User
from .serializers import UserSerializer


class UserViewSet(AppModelViewSet):
    """API endpoint users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
