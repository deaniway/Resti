from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import UserRegisterForm
from core.mixins.FormViews import SaveValidFormMixin, RenderErrorsMixin


class UserCreateView(SuccessMessageMixin, RenderErrorsMixin, SaveValidFormMixin, FormView):
    template_name = 'users/create.html'
    success_message = _("You successfully registered")
    success_url = reverse_lazy("user_login")
    form_class = UserRegisterForm
