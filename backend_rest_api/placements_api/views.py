from django.shortcuts import render
from rest_framework import generics
from .serializers import PlacementSerializer, ParentSerializer, SiblingSerializer
from .models import Placement, FosterParent, FosterSibling

# PLACEMENTS
class PlacementList(generics.ListCreateAPIView):
    queryset = Placement.objects.all().order_by('id') # tell django how to retrieve all objects from the DB, order by id ascending
    serializer_class = PlacementSerializer # tell django what serializer to use

class PlacementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Placement.objects.all().order_by('id')
    serializer_class = PlacementSerializer

# PARENTS
class ParentList(generics.ListCreateAPIView):
    queryset = FosterParent.objects.all().order_by('id')
    serializer_class = ParentSerializer

class ParentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FosterParent.objects.all().order_by('id')
    serializer_class = ParentSerializer

# SIBLINGS
class SiblingList(generics.ListCreateAPIView):
    queryset = FosterSibling.objects.all().order_by('id')
    serializer_class = SiblingSerializer

class SiblingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FosterSibling.objects.all().order_by('id')
    serializer_class = SiblingSerializer

