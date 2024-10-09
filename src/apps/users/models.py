from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _
from datetime import datetime, timezone, timedelta


class User(AbstractUser):
    TIMEZONE_CHOICES = (
        ("-3", _("Москва")),
        ("-4", _("Самара")),

    )
    timezone = models.CharField(max_length=255, default='UTC', choices=TIMEZONE_CHOICES)

    def get_current_time(self) -> datetime:
        tz = timezone( timedelta( hours=float(self.timezone)) )
        time = datetime.now( tz=tz )
        return time

    def __str__(self):
        return f"USER[ username:{self.get_username()} email:{self.email} ]"
