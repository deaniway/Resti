from django.urls import path, include
from . import views


__user_api_urlpatterns__ = [
    path(
        'users/', views.UserViewSet.as_view({
            'post': 'create'
    })),
    path(
        'users/<str:pk>', views.UserViewSet.as_view({
            'get': 'retrieve',
            'put': 'update',
            'delete': 'destroy'
    }))
]

urlpatterns = [
    path('', include( __user_api_urlpatterns__ ))
]
