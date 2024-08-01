from django import forms
from .models import Worker


class WorkerCreationForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['first_name', 'last_name', 'profession', 'bonus_salary', 'phone_number', 'telegram_link']
