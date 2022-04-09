from rest_framework import serializers 
from .models import Placement 

class PlacementSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Placement # tell django which model to use
        fields = ('id', 'name', 'start_date', 'end_date', 'location', 'foster_parents', 'foster_siblings', 'notes', 'time_stamp') # tell django which fields to include