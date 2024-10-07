from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Worker
from .forms import WorkerCreationForm
from src.core.mixins.FormViews import PassUserToFormKwargsMixin
from src.apps.businesses.models import Business
from src.core.mixins.ObjectViews import CheckPermissionsThroughBusinessMixin
from datetime import datetime


class WorkerCreationView(LoginRequiredMixin, PassUserToFormKwargsMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/create.html'
    success_url = reverse_lazy('worker_list')


class WorkerListView(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, ListView):
    model = Worker
    template_name = 'workers/list.html'
    context_object_name = 'workers'
    ordering = ['-profession']

    def get_queryset(self):
        print( self.request.user.timezone)
        # TODO: в воркер листе намутить отображаение ближайших дней рждения
        print( datetime.now( self.request.user.timezone ) )
        business_pk = self.kwargs.get('pk', None)
        queryset = super(WorkerListView, self).get_queryset()
        if business_pk: queryset = queryset.filter(business_id=business_pk)
        return queryset

    def get_context_data(self, *, object_list=None, **context):
        all_businesses = Business.viewed_by(self.request.user)
        context.update( {'businesses': all_businesses} )
        return super(WorkerListView, self).get_context_data(object_list=object_list, **context)


class WorkerUpdateView(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, PassUserToFormKwargsMixin, UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/update.html'
    success_url = reverse_lazy('worker_list')


class WorkerDeleteView(LoginRequiredMixin, CheckPermissionsThroughBusinessMixin, DeleteView):
    model = Worker
    template_name = 'workers/delete.html'
    success_url = reverse_lazy('worker_list')
