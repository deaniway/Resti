from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .models import Business
from .forms import BusinessForm
from django.contrib.auth.mixins import LoginRequiredMixin


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    form_class = BusinessForm
    template_name = 'businesses/create.html'
    success_url = reverse_lazy('business_list')


class BusinessListView(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'businesses/list.html'
    context_object_name = 'businesses'
