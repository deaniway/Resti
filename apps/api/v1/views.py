from rest_framework.permissions import AllowAny, IsAuthenticated
from .permissions import UserActionCorrectPK, IsSuperuser

from rest_framework import generics
from rest_framework.response import Response

from ..api_utils import get_queryset
from . import serializers


class UserAPIDataMixin:
    serializer_class = serializers.UserSerializer
    queryset = get_queryset('users', 'User')


class UserAPI_Register(UserAPIDataMixin, generics.CreateAPIView):
    permission_classes = [AllowAny]


class UserAPI_GetUser(UserAPIDataMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserAPI_List(UserAPIDataMixin, generics.ListAPIView):
    permission_classes = [IsSuperuser]
