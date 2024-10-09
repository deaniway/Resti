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

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update( {'user': self.request.user} )
        return kwargs
