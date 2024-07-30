from rest_framework.permissions import BasePermission, IsAuthenticated


class IsSuperuser(BasePermission):
    @staticmethod
    def is_superuser(user):
        return bool( user and user.is_superuser )

    def has_permission(self, request, view):
        return self.is_superuser( request.user )


class IsCorrectUser(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return bool(request.user.pk == obj.pk)
