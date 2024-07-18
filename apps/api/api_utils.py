from django.apps import apps
from django.db.models import Model, QuerySet


def get_model(app_label, model_name: str) -> Model:
    return apps.get_model(
        app_label=app_label, model_name=model_name
    )


def get_queryset(app_label, model_name: str) -> QuerySet:
    return get_model(app_label, model_name).objects.all()
