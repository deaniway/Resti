from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.utils.translation import gettext as _
from django.views.generic import FormView
from django.urls import reverse_lazy
from .forms import UserRegisterForm


class UserCreateView(SuccessMessageMixin, FormView):
    template_name = 'users/create.html'
    success_message = _("You successfully registered")
    success_url = reverse_lazy("index")
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        credentials = {
            'username': form.cleaned_data.get('username', None),
            'password': form.clean_password2()
        }
        user = authenticate(**credentials)
        login(self.request, user)
        return HttpResponseRedirect(self.get_success_url())
