from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_register'),
    #   add UPDATE , DELETE <-- TODO
]
