from django.shortcuts import render
from rest_framework import generics
from .serializers import PlacementSerializer
from .serializers import ParentSerializer
from .models import Placement, FosterParent

# Create your views here.
class PlacementList(generics.ListCreateAPIView):
    queryset = Placement.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PlacementSerializer # tell django what serializer to use

# CREATES PARENT LIST
class ParentList(generics.ListCreateAPIView):
    queryset = FosterParent.objects.all().order_by('id')
    serializer_class = ParentSerializer


# POSSIBLY NOT NEEDED - DELETE AFTER REFACTOR FINISHED
class PlacementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Placement.objects.all().order_by('id')
    serializer_class = PlacementSerializer