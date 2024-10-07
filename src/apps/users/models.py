from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    TIMEZONE_CHOICES = (
        ("UTC+3", _("Москва")),
        ("UTC+4", _("Самара")),

    )
    timezone = models.CharField(max_length=255, default='UTC', choices=TIMEZONE_CHOICES)

    def __str__(self):
        return f"USER[ username:{self.get_username()} email:{self.email} ]"
