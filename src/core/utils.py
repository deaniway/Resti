from django.apps import apps
from django.db.models import QuerySet


def get_queryset(app_label, model_name: str) -> QuerySet:
    return apps.get_model(app_label, model_name).objects.all()
