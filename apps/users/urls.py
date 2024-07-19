from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name='user_register'),
    path('login/', views.UserLoginView.as_view(),       name='user_login'),
    path('logout/', LogoutView.as_view(),               name='user_logout')
]
