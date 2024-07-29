from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken.views import obtain_auth_token

# from rest_framework_simplejwt.views import (
#     TokenObtainPairView,
#     TokenRefreshView,
#     TokenVerifyView
# )


urlpatterns = [
    path('admin/',              admin.site.urls),

    # path('api/token/',          TokenObtainPairView.as_view(),  name='token_obtain'),
    # path('api/token/refresh/',  TokenRefreshView.as_view(),     name='token_refresh'),
    # path('api/token/verify/',   TokenVerifyView.as_view(),      name='token_verify'),
    path('api/token/',          obtain_auth_token, name='token_obtain'),
    path('api/v1/',             include('apps.api.v1.urls')),

    path('users/',              include('apps.users.urls')),
    path('businesses/',         include('apps.businesses.urls')),
]
