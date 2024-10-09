from django.views.generic import TemplateView
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext as _
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView


class IndexTemplateView(TemplateView):
    template_name = 'index.html'


class UserLoginView(SuccessMessageMixin, LoginView):
    template_name = 'users/login.html'
    success_url = reverse_lazy("index")
    success_message = _("Вход выполнен")


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = reverse_lazy('index')
    success_message = _("Вы  вышли из системы")
