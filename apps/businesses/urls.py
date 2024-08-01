from django.urls import path
from .views import BusinessCreateView, BusinessListView

urlpatterns = [
    path('', BusinessListView.as_view(), name='business_list'),
    path('add-business/', BusinessCreateView.as_view(), name='add_business'),
]
