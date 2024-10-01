from rest_framework.generics import get_object_or_404
from src.core.utils import get_queryset
from . import serializers


class UserAPIMixin:
    serializer_class = serializers.UserSerializer
    queryset = get_queryset('users', 'User')


class GetRequestUserMixin:
    def get_object(self):
        queryset = self.filter_queryset( self.get_queryset() )

        filter_kwargs = { "pk": self.request.user.pk }
        obj = get_object_or_404(queryset, **filter_kwargs)
        self.check_object_permissions(self.request, obj)

        return obj
