from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Worker
from .forms import WorkerCreationForm


class WorkerCreationView(LoginRequiredMixin, CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/create.html'
    success_url = reverse_lazy('worker_list')


class WorkerListView(LoginRequiredMixin, ListView):
    model = Worker
    template_name = 'workers/list.html'
    context_object_name = 'workers'
    ordering = ['-profession']


class WorkerUpdateView(LoginRequiredMixin, UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/update.html'
    success_url = reverse_lazy('worker_list')


class WorkerDeleteView(LoginRequiredMixin, DeleteView):
    model = Worker
    template_name = 'workers/delete.html'
    success_url = reverse_lazy('worker_list')


class MyWorkerListView(WorkerListView):
    pass
