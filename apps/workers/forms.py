from django import forms
from .models import Worker
from ..businesses.models import Business


class WorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name','business', 'profession', 'bonus_salary', 'phone_number', 'telegram_link',]

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            # Фильтруем список бизнесов для текущего пользователя
            self.fields['business'].queryset = Business.objects.filter(businesstouser__user=user)