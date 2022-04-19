from tkinter import CASCADE
from django.db import models
from django.contrib.postgres.fields import ArrayField
from backend_rest_api import settings

# Create your models here.
class Placement(models.Model):
    num = models.CharField(max_length=155, blank=True)
    name = models.CharField(max_length=155, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    location = models.CharField(max_length=255, null=True)
    foster_parents = ArrayField(models.CharField(max_length=200, null=True), blank=True, default=list)
    foster_siblings = ArrayField(models.CharField(max_length=200, null=True), blank=True, default=list)
    notes = ArrayField(models.CharField(max_length=500, null=True), blank=True, default=list)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

class FosterParent(models.Model):
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55, null=True)
    url = models.URLField(max_length=255)
    placement = models.ForeignKey(Placement, default=None, on_delete=models.CASCADE)

class FosterSibling(models.Model):
    first_name = models.CharField(max_length=55, null=False)
    last_name = models.CharField(max_length=55, null=True)
    placement = models.ForeignKey(Placement, default=None, on_delete=models.CASCADE)