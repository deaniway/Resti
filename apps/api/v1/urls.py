from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


__api_router = DefaultRouter()
__api_router.register(r"users", views.UserViewSet)


urlpatterns = [
    path('', include( __api_router.urls ))
]
