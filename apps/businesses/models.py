from django.db import models
from django.contrib.auth import get_user_model


class Business(models.Model):
    name = models.CharField(max_length=64)


class BusinessToUser(models.Model):
    user = models.ForeignKey( get_user_model(), on_delete=models.PROTECT )
    business = models.ForeignKey( Business, on_delete=models.PROTECT )

    OWNER = 'owner'
    READONLY = 'readonly'
    MODERATOR = 'mod'

    PERMISSION_CHOICES = [
        (OWNER, 'Owner'),
        (READONLY, 'Read Only'),
        (MODERATOR, 'Moderator')
    ]
    permissions = models.CharField(max_length=10, choices=PERMISSION_CHOICES)
