from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import FormView
from django.urls import reverse_lazy

from .forms import UserRegisterForm

from core.mixins import SaveValidFormMixin, RenderErrorsMixin


__all__ = (
    "UserLoginView",
    "UserRegisterView"
)


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy("-")  # <- TODO
    success_message = _("You are logged in")


class UserRegisterView(SuccessMessageMixin, RenderErrorsMixin, SaveValidFormMixin, FormView):
    template_name = 'users/register.html'
    success_message = _("You successfully registered")
    success_url = reverse_lazy("user_login")
    form_class = UserRegisterForm
