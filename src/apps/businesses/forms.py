from django import forms
from .models import Business
from django.utils.translation import gettext_lazy as _


class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name', 'description']

        labels = {
            'name': _("Название"),
            'description': _("Описание")
        }
