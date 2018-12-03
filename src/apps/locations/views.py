from apps.core.viewsets import AppModelViewSet

from .models import Location
from .serializers import LocationSerializer


class LocationViewSet(AppModelViewSet):
    """API endpoint locations.
    """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
