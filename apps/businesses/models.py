from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _


class Business(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(
        max_length=100,
        null=True,
        help_text=_("В случае нескольких предприятий одного бренда")
    )


class BusinessToUser(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)
    business = models.ForeignKey(Business, on_delete=models.PROTECT)

    OWNER = 'owner'
    READONLY = 'readonly'
    MODERATOR = 'mod'

    PERMISSION_CHOICES = [
        (OWNER,     _('Владелец')       ),
        (MODERATOR, _('Модератор')      ),
        (READONLY,  _('Наблюдатель')    ),
    ]
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES)
