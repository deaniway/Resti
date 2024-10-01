from django.db import models
from src.apps.businesses.models import Business
from src.apps.professions.models import Profession


class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
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
        help_text="Премиальные, надбавка"
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        help_text="Телефонный номер должен быть в формате '+7(XXX)XXX-XX-XX'",
        unique=True,

    )
    telegram_link = models.URLField(
        blank=True,
        null=True,
        help_text="Введите телеграмм сотрудника для рассылки уведомлений "
    )
    business = models.ForeignKey(
        Business,
        on_delete=models.CASCADE,
        related_name='workers',
        null=True,
        blank=True,
        help_text="Выберите бизнес, к которому относится этот сотрудник."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
