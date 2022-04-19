from rest_framework import serializers 
from .models import Placement 

class PlacementSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Placement # tell django which model to use
        # THIS TELLS DJANGO WHAT DB FIELDS TO GRAB AND SEND TO THE FRONT END!!!!!(6-HOURS OF MY LIFE)
        fields = ('id', 'num', 'name', 'start_date', 'end_date', 'location',  'notes', 'time_stamp', 'user')