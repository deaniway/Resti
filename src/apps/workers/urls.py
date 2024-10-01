from django.urls import path
from .views import WorkerCreationView, MyWorkerListView ,WorkerListView, WorkerDeleteView, WorkerUpdateView

urlpatterns = [
    path('', WorkerListView.as_view(), name='worker_list'),
    path('my-workers/', MyWorkerListView.as_view(), name='my_worker_list'),
    path('create/', WorkerCreationView.as_view(), name='worker_create'),
    path('<int:pk>/update/', WorkerUpdateView.as_view(), name='worker_update'),
    path('<int:pk>/delete/', WorkerDeleteView.as_view(), name='worker_delete'),

]
