from django.db import models
from src.apps.businesses.models import Business
from src.apps.professions.models import Profession
from django.utils.translation import gettext_lazy as _


class Worker(models.Model):
    name = models.CharField(max_length=64)

    profession = models.ForeignKey(
        Profession,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    bonus_salary = models.IntegerField(
        blank=True,
        null=True,
        default=0,
        help_text=_("Премиальные, надбавка")
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text=_("Телефонный номер должен быть в формате '+7(XXX)XXX-XX-XX'"),
        unique=True,

    )
    telegram_link = models.URLField(
        blank=True,
        null=True,
        help_text=_("Введите телеграмм сотрудника для рассылки уведомлений")
    )
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='workers',
        null=True,
        blank=True,
        help_text=_("Выберите бизнес, к которому относится этот сотрудник.")
    )
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.name}"
