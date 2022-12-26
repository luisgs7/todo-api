"""Config django App"""
from django.apps import AppConfig


class TaskConfig(AppConfig):
    """Class config App"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "task"
