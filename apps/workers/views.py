from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Worker
from .forms import WorkerCreationForm


class WorkerCreationView(CreateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/create.html'
    success_url = reverse_lazy('worker_list')


class WorkerListView(ListView):
    model = Worker
    template_name = 'workers/list.html'
    context_object_name = 'workers'
    ordering = ['-profession']


class WorkerUpdateView(UpdateView):
    model = Worker
    form_class = WorkerCreationForm
    template_name = 'workers/update.html'
    success_url = reverse_lazy('worker_list')


class WorkerDeleteView(DeleteView):
    model = Worker
    template_name = 'workers/delete.html'
    success_url = reverse_lazy('worker_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_name'] = f"{self.object.first_name} {self.object.last_name}"
        return context
