from django.urls import path
from .views import WorkerCreationView, WorkerListView, WorkerDeleteView, WorkerUpdateView, WorkerListViewData

urlpatterns = [
    path('',                        WorkerListView.as_view(),       name='worker_list'),

    path('data/',                   WorkerListViewData.as_view(),   name='worker_list_data'),

    path('<int:pk>/update/',        WorkerUpdateView.as_view(),     name='worker_update'),
    path('<int:pk>/delete/',        WorkerDeleteView.as_view(),     name='worker_delete'),
    path('create/',                 WorkerCreationView.as_view(),   name='worker_create'),
]
