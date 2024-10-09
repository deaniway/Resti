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

    def form_valid(self, form):
        _response = super(BusinessCreateView, self).form_valid(form)
        self.object.link_to_user(self.request.user)
        return _response


class BusinessListView(LoginRequiredMixin, ListView):
    model = Business
    template_name = 'businesses/list.html'
    context_object_name = 'businesses'

    def get_context_data(self, *, object_list=None, **kwargs):
        object_list = Business.list_for_user(self.request.user)
        return super(BusinessListView, self).get_context_data(object_list=object_list, **kwargs)
