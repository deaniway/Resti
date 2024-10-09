from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.UserCreateView.as_view(), name='user_register'),
    #   add UPDATE , DELETE <-- TODO
]
