from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import IndexTemplateView, UserLoginView, UserLogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexTemplateView.as_view(), name='index'),

    # users
    path('users/', include('apps.users.urls')),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),

    # business
    path('business/', include('apps.businesses.urls')),

    # worker
    path('worker/', include('apps.workers.urls')),

    # API
    path('api/token/', obtain_auth_token, name='token_obtain'),
    path('api/v1/', include('apps.api.v1.urls')),
]
