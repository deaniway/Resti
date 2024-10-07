from django.urls import path
from .views import WorkerCreationView, WorkerListView, WorkerDeleteView, WorkerUpdateView

urlpatterns = [
    path('',                    WorkerListView.as_view(),       name='worker_list'),
    path('<int:pk>/filter/',    WorkerListView.as_view(),       name='worker_list_filtered'),
    path('<int:pk>/update/',    WorkerUpdateView.as_view(),     name='worker_update'),
    path('<int:pk>/delete/',    WorkerDeleteView.as_view(),     name='worker_delete'),
    path('create/',             WorkerCreationView.as_view(),   name='worker_create'),
]
