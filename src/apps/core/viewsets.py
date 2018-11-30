from typing import Tuple, TYPE_CHECKING

from django.db import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import (
    CreateModelMixin, RetrieveModelMixin, UpdateModelMixin)

if TYPE_CHECKING:
    from rest_framework.request import Request

    from apps.core.serializers import AppModelSerializer


class AppModelViewSet(
        CreateModelMixin, RetrieveModelMixin, UpdateModelMixin,
        GenericViewSet):
    """A viewset that provides create, retrieve, update actions.
    """

    def create(self, request: 'Request', *args, **kwargs) -> 'Response':
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status_code, headers = self.perform_create(serializer)

        return Response(
            serializer.data, status=status_code, headers=headers)

    def perform_create(
            self, serializer: 'AppModelSerializer') -> Tuple[int, dict]:

        try:
            serializer.save()
        except IntegrityError:
            status_code = status.HTTP_400_BAD_REQUEST
            headers = {}
        else:
            status_code = status.HTTP_200_OK
            headers = self.get_success_headers(serializer.data)

        return status_code, headers
