from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db.models import Q


class Business(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(
        max_length=100,
        null=True,
        help_text=_("В случае нескольких предприятий одного бренда")
    )

    def link_to_user(self, user):
        _link = BusinessToUser(user=user, business=self, permissions=BusinessToUser.OWNER)
        _link.save()
        return _link

    def __str__(self):
        return self.name

    @classmethod
    def list_for_user(cls, user):
        links = BusinessToUser.objects.filter(user=user)
        return [[ln.business, ln.permissions] for ln in links]

    @classmethod
    def viewed_by(cls, user, permissions=None):
        __q_filter = Q(businesstouser__user=user)

        if permissions is None:
            return cls.objects.filter(__q_filter)

        __q_permission_filter = Q( businesstouser__permissions=permissions.pop(-1) )
        for p in permissions:
            __q_permission_filter |= Q(businesstouser__permissions=p)

        return cls.objects.filter(__q_filter & __q_permission_filter)

    @classmethod
    def can_edit(cls, user):
        return cls.objects.filter( Q(businesstouser__user=user) & ~Q(businesstouser__permissions='readonly') )


class BusinessToUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)

    OWNER = 'owner'
    MODERATOR = 'mod'
    ONLY_ADD = 'add'
    READONLY = 'readonly'

    PERMISSION_CHOICES = [
        (OWNER, 'Owner'),
        (MODERATOR, 'Moderator'),
        (ONLY_ADD, 'Add and View'),
        (READONLY, 'Read Only'),
    ]
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ('user', 'business')
