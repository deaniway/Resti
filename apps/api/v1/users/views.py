from rest_framework.permissions import AllowAny, IsAuthenticated
from apps.api.v1.permissions import IsSuperuser

from rest_framework import generics
from rest_framework.response import Response

from apps.api.api_utils import get_queryset
from . import serializers
from . import mixins


class UserAPI:
    serializer_class = serializers.UserSerializer
    queryset = get_queryset('users', 'User')


class UserAPI_Register(UserAPI, generics.CreateAPIView):
    permission_classes = [AllowAny]


class UserAPI_GetUser(UserAPI, generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # GET CURRENT USER'S DATA

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserAPI_Update(UserAPI, mixins.GetRequestUserMixin, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]


class UserAPI_Delete(UserAPI, mixins.GetRequestUserMixin, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]


class UserAPI_SuperList(UserAPI, generics.ListAPIView):
    permission_classes = [IsSuperuser]


class UserAPI_SuperDelete(UserAPI, generics.DestroyAPIView):
    permission_classes = [IsSuperuser]


class UserAPI_SuperUpdate(UserAPI, generics.UpdateAPIView):
    permission_classes = [IsSuperuser]
