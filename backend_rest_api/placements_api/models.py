from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Placement(models.Model):
    num = models.CharField(max_length=155, blank=True)
    name = models.CharField(max_length=155, null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    location = models.CharField(max_length=255, null=True)
    foster_parents = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    foster_siblings = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    notes = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    time_stamp = models.DateTimeField(auto_now_add=True)