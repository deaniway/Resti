from django import forms
from .__base_mixin__ import AbstractMixin
from django.views.generic import FormView, CreateView, UpdateView


class SaveValidFormMixin(AbstractMixin):
    """mixin for FormView.
    Auto save form data to data base if form is valid"""
    __mixin_required_parents__ = (FormView, CreateView, UpdateView, )

    def form_valid(self, form: forms.ModelForm):
        form.save()
        return super(SaveValidFormMixin, self).form_valid(form)


class PassUserToFormKwargsMixin(AbstractMixin):
    __mixin_required_parents__ = (FormView, CreateView, UpdateView)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        return form_class(user=self.request.user, **self.get_form_kwargs())
