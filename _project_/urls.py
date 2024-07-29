from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/',              admin.site.urls),

    path('api/token/',          obtain_auth_token, name='token_obtain'),
    path('api/v1/',             include('apps.api.v1.urls')),

    path('users/',              include('apps.users.urls')),
]
