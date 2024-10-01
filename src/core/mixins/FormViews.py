from django import forms
from django.contrib import messages
from .__base_mixin__ import AbstractMixin
from django.views.generic import FormView


class SaveValidFormMixin(AbstractMixin):
    """mixin for FormView.
    Auto save form data to data base if form is valid"""
    __mixin_required_parents__ = (FormView, )

    def form_valid(self, form: forms.ModelForm):
        form.save()
        return super(SaveValidFormMixin, self).form_valid(form)


class RenderErrorsMixin(AbstractMixin):
    """mixin for FormView.
    Flashes error messages if form data is not valid"""
    __mixin_required_parents__ = (FormView, )

    def form_invalid(self, form: forms.ModelForm):
        messages.error(self.request, form.errors)
        return super(RenderErrorsMixin, self).form_invalid(form)
