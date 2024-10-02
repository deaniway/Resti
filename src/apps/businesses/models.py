from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _


class Business(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(
        max_length=100,
        null=True,
        help_text=_("В случае нескольких предприятий одного бренда")
    )

    def __str__(self):
        return self.name


class BusinessToUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)

    OWNER = 'owner'
    READONLY = 'readonly'
    MODERATOR = 'mod'

    PERMISSION_CHOICES = [
        (OWNER, 'Owner'),
        (READONLY, 'Read Only'),
        (MODERATOR, 'Moderator')
    ]
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES)

    class Meta:
        unique_together = ('user', 'business')
