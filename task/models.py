"""Defining the APP Task database."""
from django.db import models


class Task(models.Model):
    """Table Task Fields."""

    title = models.CharField(max_length=50)
    description = models.CharField(max_length=255)
    date = models.DateField()
    status = models.BooleanField(default=False)
