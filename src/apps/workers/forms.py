from django import forms
from .models import Worker
from ..businesses.models import Business
from django.utils.translation import gettext_lazy as _


class WorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = [
            'name',
            'date_of_birth',
            'business',
            'profession',
            'bonus_salary',
            'phone_number',
            'telegram_link'
        ]
        labels = {
            'name': _("ФИО"),
            'date_of_birth': _("Дата рождения"),
            'business': _("Заведение"),
            'profession': _('Профессия'),
            'bonus_salary': _("Премия"),
            'phone_number': _("Номер телефона"),
            'telegram_link': _("Профиль телеграм")
        }
        widgets = {
            'date_of_birth': forms.TextInput( attrs={"type": "date", } )
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['business'].queryset = Business.can_edit(user)
