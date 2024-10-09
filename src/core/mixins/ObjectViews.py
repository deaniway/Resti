from .__base_mixin__ import AbstractMixin
from django.views.generic import ListView, UpdateView, DeleteView
from apps.businesses.models import Business


class CheckPermissionsThroughBusinessMixin(AbstractMixin):
    __mixin_required_parents__ = (ListView, UpdateView, DeleteView, )

    def get_queryset(self):
        queryset = super().get_queryset()
        user = self.request.user
        return queryset.filter( business__in=Business.can_edit(user) )
