from django.urls import path
from . import views

urlpatterns = [
    # PARENTS
    path('api/parents', views.ParentList.as_view(), name='parent_list'),
    path('api/parents/<int:pk>', views.ParentDetail.as_view(), name='parent_detail'),

    #SIBLINGS
    path('api/siblings', views.SiblingList.as_view(), name='sibling_list'),
    path('api/siblings/<int:pk>', views.SiblingDetail.as_view(), name='sibling_detail'),

    # PLACEMENTS
    path('api/placements', views.PlacementList.as_view(), name='placement_list'), # api/placements will be routed to the PlacementList view for handling
    path('api/placements/<int:pk>', views.PlacementDetail.as_view(), name='placement_detail'), # api/placements will be routed to the PlacementDetail view for handling

]