from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


__api_router = DefaultRouter()
# __api_router.register(r"users", views.UserViewSet_Main)


urlpatterns = [
    path('', include( __api_router.urls )),
    path('users/register/', views.UserAPI_Register.as_view(),   name='api_user_register'),  # free access
    path('users/list/',     views.UserAPI_List.as_view(),       name='api_user_list'),      # admin only

    path('users/get/',      views.UserAPI_GetUser.as_view(),    name='api_user_get'),
    path('users/update/',   views.UserAPI_Update.as_view(),     name='api_user_update'),
    path('users/delete/',   views.UserAPI_Delete.as_view(),     name='api_user_delete'),
]
