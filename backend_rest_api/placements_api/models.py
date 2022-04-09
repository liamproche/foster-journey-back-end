from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Placement(models.Model):
    num = models.IntegerField()
    name = models.CharField(max_length=155)
    start_date = models.DateField()
    end_date = models.DateField()
    location = models.CharField(max_length=255)
    foster_parents = ArrayField(models.CharField(max_length=200), blank=True)
    foster_siblings = ArrayField(models.CharField(max_length=200), blank=True)
    notes = ArrayField(models.CharField(max_length=500), blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)