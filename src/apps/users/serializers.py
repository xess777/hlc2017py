from apps.core.serializers import AppModelSerializer

from .models import User


class UserSerializer(AppModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'gender',
            'birth_date',
        )
