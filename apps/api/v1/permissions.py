from rest_framework.permissions import IsAuthenticated


class IsSuperuser(IsAuthenticated):
    def has_permission(self, request, view):
        return super(IsSuperuser, self).has_permission(request, view) & request.user.is_superuser
