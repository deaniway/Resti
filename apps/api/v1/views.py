from rest_framework import viewsets
from ..api_utils import get_queryset
from . import serializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = get_queryset('users', 'User')
