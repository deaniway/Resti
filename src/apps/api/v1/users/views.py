from rest_framework.permissions import AllowAny, IsAuthenticated
from src.apps.api.v1.permissions import IsSuperuser

from rest_framework import generics
from rest_framework.response import Response

from . import mixins


class UserAPI_Register(mixins.UserAPIMixin, generics.CreateAPIView):
    permission_classes = [AllowAny]


class UserAPI_GetUser(mixins.UserAPIMixin, generics.ListAPIView):
    permission_classes = [IsAuthenticated]  # GET CURRENT USER'S DATA

    def list(self, request, *args, **kwargs):
        queryset = self.queryset.filter(pk=request.user.pk)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserAPI_Update(mixins.UserAPIMixin, mixins.GetRequestUserMixin, generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]


class UserAPI_Delete(mixins.UserAPIMixin, mixins.GetRequestUserMixin, generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]


class UserAPI_SuperList(mixins.UserAPIMixin, generics.ListAPIView):
    permission_classes = [IsSuperuser]


class UserAPI_SuperDelete(mixins.UserAPIMixin, generics.DestroyAPIView):
    permission_classes = [IsSuperuser]


class UserAPI_SuperUpdate(mixins.UserAPIMixin, generics.UpdateAPIView):
    permission_classes = [IsSuperuser]
