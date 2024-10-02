from django import forms
from .models import Worker
from ..businesses.models import Business
from django.utils.translation import gettext_lazy as _


class WorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'name',
            'business',
            'profession',
            'bonus_salary',
            'phone_number',
            'telegram_link'
        ]
        labels = {
            'name': _("ФИО"),
            'business': _("Заведение"),
            'profession': _('Профессия'),
            'bonus_salary': _("Премия"),
            'phone_number': _("Номер телефона"),
            'telegram_link': _("Профиль телеграм")
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['business'].queryset = Business.objects.filter(businesstouser__user=user)
