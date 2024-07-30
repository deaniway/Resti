from django.core.validators import RegexValidator
from django.db import models
from apps.professions.models import Profession


class Worker(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r'^\+7\(\d{3}\)\d{3}-\d{2}-\d{2}$',
                message="Телефонный номер должен быть в формате '+7(XXX)XXX-XX-XX', где X - цифра."
            )
        ]
    )
    telegram_link = models.URLField(
        blank=True,
        null=True,
        help_text="Необязательная ссылка на ваш профиль в Telegram."
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"