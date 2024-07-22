from django import forms
from django.contrib import messages
from .exeptions import MixinIncompatibleException


class SaveValidFormMixin:
    """mixin for FormView.
    Auto save form data to data base if form is valid"""

    def form_valid(self, form: forms.ModelForm):
        if hasattr(self, 'form_valid'):
            form.save()
            return super(SaveValidFormMixin, self).form_valid(form)

        raise MixinIncompatibleException(
            f"{self.__class__.__name__} should be only applied to FormView subclasses"
        )


class RenderErrorsMixin:
    """mixin for FormView.
    Flashes error messages if form data is not valid"""

    def form_invalid(self, form: forms.ModelForm):
        if hasattr(self, "request"):
            messages.error(self.request, form.errors)
            return super(RenderErrorsMixin, self).form_invalid(form)

        raise MixinIncompatibleException(
            f"{self.__class__.__name__} should be only applied to FormView subclasses"
        )
