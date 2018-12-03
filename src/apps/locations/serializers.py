from rest_framework.serializers import ModelSerializer

from .models import Location


class LocationSerializer(ModelSerializer):

    class Meta:
        model = Location
        fields = (
            'id',
            'place',
            'country',
            'city',
            'distance',
        )
