from django.views.generic import CreateView, ListView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Worker
from .forms import WorkerCreationForm

from core.mixins.FormViews import PassUserToFormKwargsMixin
from core.mixins.ObjectViews import CheckPermissionsThroughBusinessMixin
from ..businesses.models import Business


class WorkerCreationView(LoginRequiredMixin, PassUserToFormKwargsMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/create.html'
    success_url = reverse_lazy('worker_list')


class WorkerListView(LoginRequiredMixin, TemplateView):
    template_name = 'workers/list.html'

    def get_template_names(self):
        if Business.viewed_by(self.request.user):  # Render page only if user has at least one business
            return super(WorkerListView, self).get_template_names()
        return ['workers/nobusiness_error.html', ]

    def get_context_data(self, *, object_list=None, **context):
        all_businesses = Business.viewed_by(self.request.user)
        context.update({
            'businesses': all_businesses,
        })
        return super(WorkerListView, self).get_context_data(object_list=object_list, **context)


class WorkerListViewData(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, ListView):
    model = Worker
    template_name = 'workers/list_data.html'
    context_object_name = 'workers'
    ORDERINGS = {
        'date_of_birth': ['date_of_birth__month', 'date_of_birth__day'],
        'profession': ['-profession']
    }
    ordering = ORDERINGS['profession']

    def get_queryset(self):
        business_pk = self.request.GET.get('business_id', '0')
        queryset = super(WorkerListViewData, self).get_queryset()
        if business_pk not in {'0', '-1'}:
            return queryset.filter( business_id=int( business_pk ) )
        return queryset

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', None)
        if ordering and ordering in WorkerListViewData.ORDERINGS.keys():
            return WorkerListViewData.ORDERINGS[ordering]
        return super(WorkerListViewData, self).get_ordering()


class WorkerUpdateView(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, PassUserToFormKwargsMixin, UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/update_delete.html'
    success_url = reverse_lazy('worker_list')


class WorkerDeleteView(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, DeleteView):
    model = Worker
    template_name = 'workers/delete.html'
    success_url = reverse_lazy('worker_list')
