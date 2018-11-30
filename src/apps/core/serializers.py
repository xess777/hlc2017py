from rest_framework import serializers
from rest_framework.fields import IntegerField


class AppModelSerializer(serializers.ModelSerializer):
    id = IntegerField(read_only=False)
