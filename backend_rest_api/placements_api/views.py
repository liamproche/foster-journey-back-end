from django.shortcuts import render
from rest_framework import generics
from .serializers import PlacementSerializer, ParentSerializer, SiblingSerializer
from .models import Placement, FosterParent, FosterSibling


# PLACEMENTS
class PlacementList(generics.ListCreateAPIView):
    def get_queryset (self):
        return Placement.objects.all().filter(user=self.request.user.id)
    serializer_class = PlacementSerializer 

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