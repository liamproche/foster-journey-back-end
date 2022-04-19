from django.urls import path
from . import views

urlpatterns = [
    
    # PLACEMENTS
    path('api/placements', views.PlacementList.as_view(), name='placement_list'), # api/placements will be routed to the PlacementList view for handling
    
    # NOT YET NEEDED - LEAVE IN FOR NOW INCASE REFACTORING REQUIRES A DETAIL PATH
    path('api/placements/<int:pk>', views.PlacementDetail.as_view(), name='placement_detail'), # api/placements will be routed to the PlacementDetail view for handling

]