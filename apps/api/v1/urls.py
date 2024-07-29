from django.urls import path
from .users.views import (
    UserAPI_GetUser,
    UserAPI_Register,
    UserAPI_Update,
    UserAPI_Delete,

    UserAPI_SuperList,
    UserAPI_SuperDelete,
    UserAPI_SuperUpdate
)


urlpatterns = [
    # users
    path('users/register/',         UserAPI_Register.as_view(),         name='api_user_register'),
    path('users/get/',              UserAPI_GetUser.as_view(),          name='api_user_get'),
    path('users/update/',           UserAPI_Update.as_view(),           name='api_user_update'),
    path('users/delete/',           UserAPI_Delete.as_view(),           name='api_user_delete'),

    # users. admin only
    path('users/list/',             UserAPI_SuperList.as_view(),        name='api_sudo_user_list'),
    path('users/update/<int:pk>/',  UserAPI_SuperUpdate.as_view(),      name='api_sudo_user_update'),
    path('users/delete/<int:pk>/',  UserAPI_SuperDelete.as_view(),      name='api_sudo_user_delete'),
]
