from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_message = _("You are logged in")
